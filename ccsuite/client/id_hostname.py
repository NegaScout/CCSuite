from ccsuite.client.exec_base import CCClientExecBase
from ccsuite.client.id_base import CCClientIDBase


class CCClientIDHostname(CCClientIDBase):
    def __init__(self, executor: CCClientExecBase):
        super().__init__()
        self.executor = executor

    def id(self):
        return self.executor.exec("hostname").decode().strip()
