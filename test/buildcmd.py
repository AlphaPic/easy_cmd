from api import command

class buildCmd:
    def __init__(self):
        self.direct = command.Command(cmd='')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


with buildCmd() as bc:
    bc.direct.create_Direct()