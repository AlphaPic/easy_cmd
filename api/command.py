
class Command(object):
    def __init__(self,cmd=None,parent=None,desc=None,func=None,root=None,identity=None):
        self._command               = cmd
        self._id                    = identity
        self._parent_command_id     = parent
        self._description           = desc
        self._function              = func
        self._root_command_id       = root

    #创建目录
    def create_Direct(self):
        print(self.name)

    #非法指令
    def illeagle_cmd(self):
        return True