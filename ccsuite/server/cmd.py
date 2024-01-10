import time
def command_create(command_kind, *args):
    command_obj = {'command': {}}
    command_obj['command']['kind'] = command_kind
    command_obj['command']['args'] = list(args)
    command_obj['command']['id'] = int(time.time())
    command_obj['command']['timestamp'] = int(time.time())
    return command_obj

if __name__ == '__main__':
    print(command_create('id'))