from ccsuite.ccchanel.ccchanel_base import CCChanelBase
from ccsuite.ccchanel.ccchanel_file import CCChanelFile
from ccsuite.steno.steno_base import CCStenoBase


def log_append(ccchanel: CCChanelBase, remote_path, entry, steno_: CCStenoBase):
    log = log_read(ccchanel, remote_path, steno_)
    if log is None:
        return
    log += [entry]
    payload = steno_.encode(log)
    ccchanel.write(payload, remote_path)
    print(f'LOG: appended {entry} to {remote_path}')


def log_read(ccchanel: CCChanelBase, remote_path, steno_: CCStenoBase):
    if not ccchanel.exists(remote_path):
        return None
    bytes_read = ccchanel.read(remote_path)
    payload = steno_.decode(bytes_read)
    return payload


def log_init(ccchanel: CCChanelBase, remote_path, steno_: CCStenoBase):
    payload = steno_.encode([])
    ccchanel.write(payload, remote_path)
    print(f'LOG: init {remote_path}')


if __name__ == '__main__':
    path_ = '/tmp/log.txt'
    cch = CCChanelFile()
    steno_ = CCStenoBase()
    log_init(cch, path_, steno_)
    print(log_read(cch, path_, steno_))
    log_append(cch, path_, 'Hello World!', steno_)
    print(log_read(cch, path_, steno_))
    log_append(cch, path_, 'Hello World! For the second time', steno_)
    print(log_read(cch, path_, steno_))
