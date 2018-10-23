from api import command as c
from api import Tree as t

class Command_List:
    def __init__(self):
        self.__commands         = {}
        self.__commands_root    = t.TreeNode()
        #
        self.__cmd              = c.Command(identity=-1)
        self.__commands_root._root_cmd = self.__cmd

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def put_command(self,cmd = None):
        if isinstance(cmd,c.Command):
            if cmd.illeagle_cmd() is True:
                raise Exception('illeagal command %s' % cmd._command)

            #没有根目录
            if cmd._root_command_id is None:
                if cmd._parent_command_id is None:
                    cmd._parent_command_id          = cmd._id
                    cmd._root_command_id            = cmd._id
                    #
                    self.__commands[cmd._id]        = cmd
                    self.__commands_root._child_cmd.append(cmd)
                else:
                    parent_cmd  = self.__get_parent_command(self.__commands_root,cmd)
                    if parent_cmd is None:
                        cmd._root_command_id        = cmd._id
                        self.__commands[cmd._id]    = cmd
                        self.__commands_root._child_cmd.append(cmd)
                    else:
                        cmd._root_command_id        = parent_cmd._id
                        parent_cmd._child_cmd.append(cmd)
            else:
                parent_cmd = self.__get_parent_command(self.__commands_root,cmd)
                if cmd._parent_command_id is None or cmd._parent_command_id == parent_cmd._id:
                    parent_cmd._child_cmd.append(cmd)
                else:
                    return -1
            return cmd._id
        else:
            raise Exception('unknow type [ %s ]' % cmd)

    #获取父评论
    def __get_parent_command(self,root,cmd):
        if root._root_cmd._id == cmd._parent_command_id:
            return root
        else:
            if len(root._child_cmd) != 0:
                for child in root._child_cmd:
                    child = self.__get_parent_command(child,cmd)
                    if child is not None:
                        return child
            else:
                return None

    #显示指令树
    def show_command_tree(self):
