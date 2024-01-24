class CCChanelBase(object):
    def write(self, data: bytes, *args, **kwargs) -> None:
        pass

    def read(self, identifier: str, *args, **kwargs) -> bytes:
        pass

    def list(self, identifier: str, *args, **kwargs) -> [str]:
        pass

    def exists(self, identifier: str, *args, **kwargs) -> bool:
        pass
