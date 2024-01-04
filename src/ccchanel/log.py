import ccchanel.file as file
def log_append(dbx, path, entry):
    log = log_read(dbx, path)
    log += [entry]
    payload = file.encode_to_bytes(log)
    file.upload_file_fp(dbx, payload, path)
    print(f'LOG: appended {entry} to {path}')
def log_read(dbx, path):
    bytes = file.download_file(dbx, path)
    try:
        payload = file.decode_from_bytes(bytes)
        return payload
    except Exception:
        return None
def log_init(dbx, path):
    payload = file.encode_to_bytes([])
    file.upload_file_fp(dbx, payload, path)
    print(f'LOG: init {path}')

if __name__ == '__main__':
    import dropbox_api
    dbx = dropbox_api.dropbox_login()
    log_init(dbx, '/log.txt')
    print(log_read(dbx, '/log.txt'))
    log_append(dbx, '/log.txt', 'Hello World!')
    print(log_read(dbx, '/log.txt'))
    log_append(dbx, '/log.txt', 'Hello World! For the second time')
    print(log_read(dbx, '/log.txt'))
