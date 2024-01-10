from .exec import execute_arbitrary_command


def id():
    id = execute_arbitrary_command("hostname").decode().strip()
    return id
