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

def get_done_with_id(log, id):
    for log_entry in reversed(log):
        if log_entry.get('done', False) and log_entry['done'].get('id', False) == id:
            return log_entry['done']
    return None

def help_string():
    help_string = ""
    help_string += "Server has two command modes, 'local' and 'remote' which have to be prepended with each entry\n"
    help_string += "Commands for local:\n"
    help_string += "\tget <target (dropbox path, has to begin with /)> # downloads the file from dropbox to /tmp\n"
    help_string += "\tcat <target (dropbox path, has to begin with /)> # cats log contained within the file\n"
    help_string += "\tonline # prints list of online bots\n"
    help_string += "\tresult <task_id> # prints the payload, which the client appended to the log after finishing the task\n"
    help_string += "Commands for remote:\n"
    help_string += "\tupload <bot_local_path (unix path)> # uploads file to dropbox as is\n"
    help_string += "\t<remote_path or command> <args*> # executes arbitrary command\n"

    return help_string
if __name__ == '__main__':
    log = [{'alive': {'timestamp': 1704385737}}, {'ping': {'timestamp': 1704385758}}]
    log = [{'alive': {'timestamp': 1704385737}}, {'ping': {'timestamp': 1704385758}}, {'ping': {'timestamp': int(time.time())}}]
    log = [{'alive': {'timestamp': 1704385737}}, {'ping': {'timestamp': 1704385758}}, {'ping': {'timestamp': 1704385780}}, {'alive': {'timestamp': 1704387238}}, {'ping': {'timestamp': 1704387258}}, {'ping': {'timestamp': 1704387279}}, {'ping': {'timestamp': 1704387299}}, {'ping': {'timestamp': 1704387320}}, {'ping': {'timestamp': 1704387340}}, {'ping': {'timestamp': 1704387361}}, {'ping': {'timestamp': 1704387381}}, {'alive': {'timestamp': 1704387485}}, {'ping': {'timestamp': 1704387506}}, {'ping': {'timestamp': 1704387527}}, {'ping': {'timestamp': 1704387548}}, {'ping': {'timestamp': 1704387568}}, {'ping': {'timestamp': 1704387589}}, {'ping': {'timestamp': 1704387609}}, {'ping': {'timestamp': 1704387630}}, {'ping': {'timestamp': 1704387650}}, {'ping': {'timestamp': 1704387671}}, {'ping': {'timestamp': 1704387692}}, {'ping': {'timestamp': 1704387713}}, {'ping': {'timestamp': 1704387733}}, {'ping': {'timestamp': 1704387754}}, {'ping': {'timestamp': 1704387775}}, {'ping': {'timestamp': 1704387796}}, {'ping': {'timestamp': 1704387817}}, {'ping': {'timestamp': 1704387837}}, {'ping': {'timestamp': 1704387858}}, {'ping': {'timestamp': 1704387879}}, {'ping': {'timestamp': 1704387899}}, {'ping': {'timestamp': 1704387919}}, {'ping': {'timestamp': 1704387940}}, {'ping': {'timestamp': 1704387961}}, {'ping': {'timestamp': 1704387981}}, {'ping': {'timestamp': 1704388002}}, {'ping': {'timestamp': 1704388023}}, {'ping': {'timestamp': 1704388043}}, {'ping': {'timestamp': 1704388064}}, {'ping': {'timestamp': 1704388085}}, {'ping': {'timestamp': 1704388105}}, {'ping': {'timestamp': 1704388125}}, {'ping': {'timestamp': 1704388146}}, {'ping': {'timestamp': 1704388166}}, {'ping': {'timestamp': 1704388187}}, {'ping': {'timestamp': 1704388207}}, {'ping': {'timestamp': 1704388228}}, {'ping': {'timestamp': 1704388248}}, {'ping': {'timestamp': 1704388269}}, {'ping': {'timestamp': 1704388290}}, {'ping': {'timestamp': 1704388310}}, {'ping': {'timestamp': 1704388330}}, {'command': {'kind': 'whoami', 'args': [], 'id': 1704388352, 'timestamp': 1704388352}}, {'ping': {'timestamp': 1704388372}}, {'done': {'id': 1704388352, 'payload': 'honza\n'}}, {'ping': {'timestamp': 1704388398}}, {'ping': {'timestamp': 1704388419}}, {'ping': {'timestamp': 1704388439}}, {'ping': {'timestamp': 1704388460}}, {'ping': {'timestamp': 1704388481}}, {'ping': {'timestamp': 1704388501}}, {'ping': {'timestamp': 1704388522}}, {'ping': {'timestamp': 1704388543}}, {'ping': {'timestamp': 1704388563}}, {'ping': {'timestamp': 1704388583}}, {'ping': {'timestamp': 1704388604}}, {'command': {'kind': 'whoami', 'args': [], 'id': 1704388627, 'timestamp': 1704388627}}, {'ping': {'timestamp': 1704388647}}, {'done': {'id': 1704388627, 'payload': 'honza\n'}}, {'ping': {'timestamp': 1704388675}}, {'ping': {'timestamp': 1704388695}}, {'command': {'kind': 'whoami', 'args': [], 'id': 1704388705, 'timestamp': 1704388705}}, {'ping': {'timestamp': 1704388716}}, {'done': {'id': 1704388705, 'payload': 'honza\n'}}, {'ping': {'timestamp': 1704388741}}, {'ping': {'timestamp': 1704388761}}, {'ping': {'timestamp': 1704388782}}, {'command': {'kind': 'whoami', 'args': [], 'id': 1704388788, 'timestamp': 1704388788}}, {'ping': {'timestamp': 1704388803}}, {'done': {'id': 1704388788, 'payload': 'honza\n'}}, {'ping': {'timestamp': 1704388828}}, {'ping': {'timestamp': 1704388848}}, {'ping': {'timestamp': 1704388869}}, {'ping': {'timestamp': 1704388889}}, {'ping': {'timestamp': 1704388910}}, {'ping': {'timestamp': 1704388931}}, {'ping': {'timestamp': 1704388952}}, {'ping': {'timestamp': 1704388973}}, {'ping': {'timestamp': 1704388993}}, {'ping': {'timestamp': 1704389014}}, {'ping': {'timestamp': 1704389034}}, {'ping': {'timestamp': 1704389054}}, {'ping': {'timestamp': 1704389077}}, {'ping': {'timestamp': 1704389098}}, {'ping': {'timestamp': 1704389118}}, {'ping': {'timestamp': 1704389139}}, {'command': {'kind': 'whoami', 'args': [], 'id': 1704389163, 'timestamp': 1704389163}}, {'ping': {'timestamp': 1704389181}}, {'done': {'id': 1704389163, 'payload': 'honza\n'}}, {'ping': {'timestamp': 1704389206}}, {'ping': {'timestamp': 1704389226}}, {'ping': {'timestamp': 1704389247}}, {'ping': {'timestamp': 1704389267}}, {'ping': {'timestamp': 1704389288}}, {'ping': {'timestamp': 1704389309}}, {'ping': {'timestamp': 1704389330}}, {'ping': {'timestamp': 1704389350}}, {'ping': {'timestamp': 1704389372}}, {'ping': {'timestamp': 1704389392}}, {'ping': {'timestamp': 1704389414}}, {'ping': {'timestamp': 1704389434}}, {'ping': {'timestamp': 1704389455}}, {'ping': {'timestamp': 1704389476}}, {'ping': {'timestamp': 1704389497}}, {'ping': {'timestamp': 1704389518}}, {'ping': {'timestamp': 1704389539}}, {'ping': {'timestamp': 1704389559}}, {'ping': {'timestamp': 1704389580}}, {'ping': {'timestamp': 1704389600}}, {'ping': {'timestamp': 1704389622}}, {'ping': {'timestamp': 1704389644}}, {'ping': {'timestamp': 1704389664}}, {'ping': {'timestamp': 1704389685}}, {'ping': {'timestamp': 1704389706}}, {'ping': {'timestamp': 1704389728}}, {'ping': {'timestamp': 1704389749}}, {'ping': {'timestamp': 1704389771}}, {'ping': {'timestamp': 1704389792}}, {'ping': {'timestamp': 1704389812}}, {'ping': {'timestamp': 1704389833}}, {'command': {'kind': 'whoami', 'args': [], 'id': 1704389847, 'timestamp': 1704389847}}, {'ping': {'timestamp': 1704389855}}, {'done': {'id': 1704389847, 'payload': 'honza\n'}}, {'ping': {'timestamp': 1704389880}}, {'ping': {'timestamp': 1704389900}}, {'ping': {'timestamp': 1704389932}}, {'ping': {'timestamp': 1704389953}}, {'ping': {'timestamp': 1704389975}}]
    print(get_done_with_id(log, 1704388352))
