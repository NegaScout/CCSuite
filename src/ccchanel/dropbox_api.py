import dropbox, os
def dropbox_login():
    dbx = dropbox.Dropbox(os.environ['DROPBOX_TOKEN'])
    return dbx

if __name__ == '__main__':
    dbx = dropbox_login()
