
def parse_command():
    input_line = input('> ')
    command_parts = input_line.split()
    prefix = command_parts[0]
    if prefix in ['local', 'remote']:
        return create_repl_command(prefix, command_parts[1:])
    return None


def create_repl_command(kind, command_list):
    cmd_list_len = len(command_list)
    if kind not in ['local', 'remote']:
        return None
    if kind == 'local' and cmd_list_len < 1:
        return None
    elif kind == 'remote' and cmd_list_len < 2:
        return None

    command = {kind: {}}
    if kind == 'remote':
        command[kind]['target'] = command_list[0]
        command[kind]['command'] = command_list[1]
        command[kind]['args'] = command_list[2:]
    else:
        command[kind]['command'] = command_list[0]
        command[kind]['args'] = command_list[1:]

    return command


if __name__ == '__main__':
    while True:
        command = parse_command()
        print(command)
