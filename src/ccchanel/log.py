import ccchanel.file as ccfile
def log_append(dbx, remote_path, entry):
    log = log_read(dbx, remote_path)
    if log is None:
        return
    log += [entry]
    payload = ccfile.encode_to_bytes(log)
    ccfile.upload_file_fp(dbx, payload, remote_path)
    print(f'LOG: appended {entry} to {remote_path}')
def log_read(dbx, remote_path):
    if not ccfile.file_exists(dbx, remote_path):
        return None
    bytes = ccfile.download_file(dbx, remote_path)
    try:
        payload = ccfile.decode_from_bytes(bytes)
        return payload
    except Exception:
        return None
def log_init(dbx, remote_path):
    payload = ccfile.encode_to_bytes([])
    ccfile.upload_file_fp(dbx, payload, remote_path)
    print(f'LOG: init {remote_path}')

if __name__ == '__main__':
    import dropbox_api
    dbx = dropbox_api.dropbox_login()
    log_init(dbx, '/log.txt')
    print(log_read(dbx, '/log.txt'))
    log_append(dbx, '/log.txt', 'Hello World!')
    print(log_read(dbx, '/log.txt'))
    log_append(dbx, '/log.txt', 'Hello World! For the second time')
    print(log_read(dbx, '/log.txt'))
