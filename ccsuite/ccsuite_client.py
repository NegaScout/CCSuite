import time
from .client.client import CCClient
from ccchanel.ccchanel_file import CCChanelFile
from ccchanel.log import log_append
from steno.steno_base import CCStenoBase
from .client import payloads as cpayload


def main():
    client = CCClient(CCChanelFile, CCStenoBase)
    client.run()


if __name__ == "__main__":
    main()
