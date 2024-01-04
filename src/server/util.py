import time

def get_last_ping(log):
    for log_entry in reversed(log):
        if log_entry.get('ping', False):
            return log_entry['ping']
        elif log_entry.get('alive', False):
            return log_entry['alive']
    return None

def is_online(log, age_treshold=30):
    last_ping = get_last_ping(log)
    if last_ping is not None:
        diff = int(time.time()) - last_ping['timestamp']
        return age_treshold >= diff >= 0
    return False

if __name__ == '__main__':
    log = [{'alive': {'timestamp': 1704385737}}, {'ping': {'timestamp': 1704385758}}]
    log = [{'alive': {'timestamp': 1704385737}}, {'ping': {'timestamp': 1704385758}}, {'ping': {'timestamp': int(time.time())}}]
    print(is_online(log))