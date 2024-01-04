import dropbox, json
from io import BytesIO

from stegano import lsb as steg
def list_files(dbx, path):
    # stolen and modified from https://github.com/dropbox/dropbox-sdk-python/blob/main/example/updown.py
    try:
        res = dbx.files_list_folder(path)
    except dropbox.exceptions.ApiError as err:
        print('Folder listing failed for', path, '-- assumed empty:', err)
        return {}
    else:
        rv = {}
        for entry in res.entries:
            rv[entry.name] = entry
        return rv

def upload_file_fp(dbx, file_handle, name):
    # stolen and modified from https://github.com/dropbox/dropbox-sdk-python/blob/main/example/updown.py
    print(f"FILE: executing fp upload {name}")
    mode = dropbox.files.WriteMode.overwrite
    data = file_handle.read()
    try:
        res = dbx.files_upload(data, name, mode, mute=True)
    except dropbox.exceptions.ApiError as err:
        print('*** API error', err)
        return None
    return res
def upload_file(dbx, local_path, name):
    print(f"FILE: executing upload {local_path} as {name}")
    with open(local_path, 'rb') as file_handle:
        upload_file_fp(dbx, file_handle, name)
def download_file(dbx, remote_path):
    # stolen and modified from https://github.com/dropbox/dropbox-sdk-python/blob/main/example/updown.py
    try:
        md, res = dbx.files_download(remote_path)
    except dropbox.exceptions.HttpError as err:
        print('*** HTTP error', err)
        return None
    data = res.content
    return data
def download_file_as(dbx, path_remote, path_local):
    # stolen and modified from https://github.com/dropbox/dropbox-sdk-python/blob/main/example/updown.py
    print(f'FILE: file r:{path_remote} downloading to l:{path_local}')
    with open(path_local, 'wb') as file_handle:
        file_handle.write(download_file(dbx, path_remote))

def encode_to_bytes(payload: object, image_path='./ccchanel/resources/image.png'):
    payload = json.dumps(payload)
    mem_fp = BytesIO()
    stenoed_image = steg.hide(image_path, payload)
    stenoed_image.save(mem_fp, format='PNG')
    mem_fp.seek(0)
    return mem_fp
def decode_from_bytes(bytes):
    mem_fp = BytesIO(bytes)
    payload_raw = steg.reveal(mem_fp)
    payload = json.loads(payload_raw)
    return payload

if __name__ == '__main__':
    out_path = '/home/honza/PycharmProjects/CCSuite/src/ccchanel/resources/image.png'
    bts = encode_to_bytes(['payload'], image_path=out_path)
    ret = decode_from_bytes(bts.read())
    print(ret)
