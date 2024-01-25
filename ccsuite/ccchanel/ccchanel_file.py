from ccsuite.ccchanel.ccchanel_base import CCChanelBase
from os import listdir, path


class CCChanelFile(CCChanelBase):
    def write(self, data: bytes, *args, **kwargs) -> None:
        f_path, = args
        with open(f_path, "wb") as fp:
            fp.write(data)
        return

    def read(self, identifier: str, *args, **kwargs) -> bytes:
        with open(identifier, "rb") as fp:
            return fp.read()

    def list(self, identifier: str, *args, **kwargs) -> [str]:
        return listdir(identifier)

    def exists(self, identifier: str, *args, **kwargs) -> bool:
        return path.basename(identifier) in self.list(path.dirname(identifier), *args, **kwargs)


if __name__ == '__main__':
    file = '/tmp/ccchanel.txt'
    obj = b'sada'
    base = CCChanelFile()
    print(base.write(obj, file))
    print(base.read(file))
    print(base.list('/tmp'))
    print(base.exists(file))
