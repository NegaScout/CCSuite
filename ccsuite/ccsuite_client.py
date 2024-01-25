from .client.client import CCClient
from ccchanel.ccchanel_file import CCChanelFile
from steno.steno_base import CCStenoBase


def main():
    client = CCClient(CCChanelFile, CCStenoBase)
    client.run()


if __name__ == "__main__":
    main()
