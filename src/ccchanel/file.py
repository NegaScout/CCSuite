import dropbox
def list_files(dbx, path, *args):
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

def upload_file(dbx, path, name, *args):
    # stolen and modified from https://github.com/dropbox/dropbox-sdk-python/blob/main/example/updown.py
    mode = dropbox.files.WriteMode.overwrite
    with open(path, 'rb') as file_handle:
        data = file_handle.read()
    try:
        res = dbx.files_upload(data, name, mode, mute=True)
    except dropbox.exceptions.ApiError as err:
        print('*** API error', err)
        return None
    return res

def download_file(dbx, path, *args):
    # stolen and modified from https://github.com/dropbox/dropbox-sdk-python/blob/main/example/updown.py
    try:
        md, res = dbx.files_download(path)
    except dropbox.exceptions.HttpError as err:
        print('*** HTTP error', err)
        return None
    data = res.content
    return data

def encode_file(path, output_path, payload, *args):
    pass
def decode_file(path, *args):
    pass
