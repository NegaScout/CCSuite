import ccchanel.log as cclog
import ccchanel.dropbox_api as cc_api
import server.cmd
def check_pong(dbx, path):
    log = cclog.log_read(dbx, path)

def dispatch_command(dbx, path, command, *args):
    cclog.log_append(dbx, path, server.cmd.command_create(command, *args))

if __name__ == "__main__":
    dbx = cc_api.dropbox_login()
    dispatch_command(dbx, "/log.txt", 'id')
