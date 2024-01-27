from ccsuite.ccchanel.ccchanel_base import CCChanelBase
import os


class CCChanelFile(CCChanelBase):
    def write(self, data: bytes, *args, **kwargs) -> None:
        if len(args) == 0:
            raise TypeError("number of *args has to be at least one")

        f_path, = args
        with open(f_path, "wb") as fp:
            fp.write(data)
        return

    def read(self, identifier: str, *args, **kwargs) -> bytes:
        with open(identifier, "rb") as fp:
            return fp.read()

    def list(self, identifier: str, *args, **kwargs) -> [str]:
        return os.listdir(identifier)

    def exists(self, identifier: str, *args, **kwargs) -> bool:
        return os.path.basename(identifier) in self.list(os.path.dirname(identifier), *args, **kwargs)


if __name__ == '__main__':
    file = '/tmp/ccchanel.txt'
    obj = b'sada'
    base = CCChanelFile()
    print(base.write(obj, file))
    print(base.read(file))
    print(base.list('/tmp'))
    print(base.exists(file))
