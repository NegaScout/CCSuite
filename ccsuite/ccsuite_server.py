from ccsuite.ccchanel.ccchanel_file import CCChanelFile
from ccsuite.server.server import CCServer
from ccsuite.steno.steno_base import CCStenoBase


def main():
    client = CCServer(CCChanelFile, CCStenoBase)
    client.run()


if __name__ == "__main__":
    main()
