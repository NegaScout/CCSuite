import subprocess, re
def get_exec_paths(exec_names: list):
    pass
    # so far did not need absolute paths
    exec_paths = []
    for exec_name in exec_names:
        whereis = execute_arbitrary_command('whereis', exec_name).decode()
        exec_paths += []
    return exec_paths

def execute_arbitrary_command(path, *args):
    exec_payload = ' '.join([path] + list(*args))
    exec_return = subprocess.run(exec_payload, capture_output=True)
    return exec_return.stdout

def execute_command(path, *args):
    if path == 'GET':
        raise Exception('Not implemented')
    return execute_arbitrary_command(path, *args)

if __name__ == '__main__':
    ret = execute_arbitrary_command('whoami')
    print(ret)