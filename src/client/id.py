import client.exec as cexec
def id():
    id = cexec.execute_arbitrary_command("hostname").decode()
    return id
