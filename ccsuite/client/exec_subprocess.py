import subprocess

from ccsuite.client.exec_base import CCClientExecBase


class CCClientExecSubprocess(CCClientExecBase):
    def __init__(self, *args, **kwargs):
        super().__init__()

    def exec(self, *args, **kwargs):
        args_num = len(args)
        local_path = args[0]
        if args_num > 1:
            local_args = args[1]
        else:
            local_args = tuple()
        print(f"EXEC: executing {local_path} {local_args}")
        exec_payload = [local_path] + list(local_args)
        exec_return = subprocess.run(exec_payload, capture_output=True)
        return exec_return.stdout
