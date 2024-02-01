def parse_command(input_stream):
    print('> ', end='')
    input_line = input_stream.readline()
    match len(input_line):
        case 1:
            return create_repl_command_noop()
        case 0:
            return create_repl_command_exit()
    command_parts = input_line.strip().split()
    prefix = command_parts[0]
    match prefix:
        case 'local':
            return create_repl_command_local(command_parts[1:])
        case 'remote':
            return create_repl_command_remote(command_parts[1:])
        case _:
            return create_repl_command_noop()


def create_repl_command_remote(command_list):
    if len(command_list) < 2:
        return create_repl_command_noop()
    kind = 'remote'
    command = {'kind': kind, 'payload': {}}
    command['payload']['target'] = command_list[0]
    command['payload']['command'] = command_list[1]
    command['payload']['args'] = command_list[2:]
    return command


def create_repl_command_local(command_list):
    if len(command_list) < 1:
        return create_repl_command_noop()
    kind = 'local'
    command = {'kind': kind, 'payload': {}}
    command['payload']['command'] = command_list[0]
    command['payload']['args'] = command_list[1:]
    return command


def create_repl_command_noop():
    return {'kind': 'noop', 'payload': {}}


def create_repl_command_exit():
    return {'kind': 'exit', 'payload': {}}


if __name__ == '__main__':
    import sys

    command = parse_command(sys.stdin)
    print(command)
    while command['kind'] != 'exit':
        command = parse_command(sys.stdin)
        print(command)
