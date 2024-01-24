from json import loads, dumps


class CCStenoBase(object):
    def encode(self, payload: object, *args, **kwargs) -> bytes:
        return dumps(payload).encode()

    def decode(self, payload: bytes, *args, **kwargs) -> object:
        return loads(payload.decode())

if __name__ == '__main__':
    obj = ['hi']
    base = CCStenoBase()
    print(base.encode(obj))
    print(base.decode(base.encode(obj)))
