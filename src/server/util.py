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

def print_help():
    help_string = ""
    help_string += "Server has two command modes, 'local' and 'remote' which have to be prepended with each entry\n"
    help_string += "Commands for local:\n"
    help_string += "\tget <target (dropbox path, has to begin with /)> # downloads the file from dropbox to /tmp\n"
    help_string += "\tcat <target (dropbox path, has to begin with /)> # cats log contained within the file\n"
    help_string += "\tonline # prints list of online bots\n"
    help_string += "Commands for remote:\n"
    help_string += "\tupload <bot_local_path (unix path)> # uploads file to dropbox as is\n"
    help_string += "\t<remote_path or command> <args*> # executes arbitrary command\n"

    return help_string
if __name__ == '__main__':
    log = [{'alive': {'timestamp': 1704385737}}, {'ping': {'timestamp': 1704385758}}]
    log = [{'alive': {'timestamp': 1704385737}}, {'ping': {'timestamp': 1704385758}}, {'ping': {'timestamp': int(time.time())}}]
    print(is_online(log))