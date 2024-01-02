import json

def log_append(path, entry):
    log = log_read(path)
    log += [entry]
    with open(path, 'w') as file_handle:
        json.dump(log, file_handle)

def log_read(path):
    with open(path, 'r') as file_handle:
        return json.load(file_handle)

def log_create(path):
    with open(path, 'w') as file_handle:
        json.dump([], file_handle)

if __name__ == '__main__':
    log_create('resources/log')
    print(log_read('resources/log'))
    log_append('resources/log', 'Hello World!')
    print(log_read('resources/log'))