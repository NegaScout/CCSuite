import time


def message_create_command(message_id, command_kind, *args):
    command_obj = {'command': {}}
    command_obj['command']['kind'] = command_kind
    command_obj['command']['args'] = list(args)
    command_obj['command']['id'] = message_id
    command_obj['command']['timestamp'] = int(time.time())
    return command_obj


def message_create_ping():
    ping_obj = {'ping': {}}
    ping_obj['ping']['timestamp'] = int(time.time())
    return ping_obj


def message_create_alive():
    alive_obj = {'alive': {}}
    alive_obj['alive']['timestamp'] = int(time.time())
    return alive_obj


def message_create_done(job_id, payload):
    alive_obj = {'done': {'id': job_id, 'payload': payload}}
    return alive_obj


if __name__ == '__main__':
    print(message_create_command(None, 'id'))
