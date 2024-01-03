import time
def ping_create():
    ping_obj = {'ping': {}}
    ping_obj['ping']['timestamp'] = int(time.time())
    return ping_obj

def alive_create():
    alive_obj = {'alive': {}}
    alive_obj['alive']['timestamp'] = int(time.time())
    return alive_obj

def done_create(id):
    alive_obj = {'done': {'id': int(time.time())}}
    return alive_obj
