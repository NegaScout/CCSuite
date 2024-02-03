from client.client_base import CCClient
from client.id_hostname import CCClientIDHostname
from client.exec_subprocess import CCClientExecSubprocess
from ccchanel.ccchanel_file import CCChanelFile
from steno.steno_base import CCStenoBase


def main():
    executor = CCClientExecSubprocess()
    id_provider = CCClientIDHostname(executor)
    client = CCClient(CCChanelFile(), CCStenoBase(), executor, id_provider)
    client.run()


if __name__ == "__main__":
    main()
