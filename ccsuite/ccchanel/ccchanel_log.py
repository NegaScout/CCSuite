from ccsuite.ccchanel.ccchanel_base import CCChanelBase
from ccsuite.ccchanel.ccchanel_file import CCChanelFile
from ccsuite.steno.steno_base import CCStenoBase


def log_append(ccchanel: CCChanelBase, steno_: CCStenoBase, entry, remote_path, *args, **kwargs):
    log = log_read(ccchanel, steno_, remote_path)
    if log is None:
        return
    log += [entry]
    payload = steno_.encode(log)
    ccchanel.write(payload, remote_path, *args, **kwargs)
    print(f'LOG: appended {entry} to {remote_path}')


def log_read(ccchanel: CCChanelBase, steno_: CCStenoBase, remote_path, *args, **kwargs):
    if not ccchanel.exists(remote_path, *args, **kwargs):
        return None
    bytes_read = ccchanel.read(remote_path)
    payload = steno_.decode(bytes_read)
    return payload


def log_init(ccchanel: CCChanelBase, steno_: CCStenoBase, remote_path, *args, **kwargs):
    payload = steno_.encode([])
    ccchanel.write(payload, remote_path, *args, **kwargs)
    print(f'LOG: init {remote_path}')


if __name__ == '__main__':
    path_ = '/tmp/log.txt'
    cch = CCChanelFile()
    steno_ = CCStenoBase()
    log_init(cch, steno_, path_)
    print(log_read(cch, steno_, path_))
    log_append(cch, steno_, 'Hello World!', path_)
    print(log_read(cch, steno_, path_))
    log_append(cch, steno_, 'Hello World! For the second time', path_)
    print(log_read(cch, steno_, path_))
