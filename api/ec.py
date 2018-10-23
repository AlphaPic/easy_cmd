from api import command as c
from api import title as t
from api import command_list as cl
from api import identity_numbers as idn

class Easy_Command:
    def __init__(self,title = 'easy command'):
        self.__commands         = cl.Command_List()
        self.__title            = t.Title()

        #title
        self.__title._set_title(title)

        #id
        self.__id_class         = idn.Identity_Numbers()
        self.__id_iter          = iter(self.__id_class)

    def set_title(self,title = 'easy command'):
        self.__title._set_title(title)

    def __default_method(self):
        print('current command doesn\' set method')

    #创建指令
    #return : -1 创建失败 , > 0 评论id
    def create_command(self,
                       parentCommand = None,
                       command       = None,
                       description   = None,
                       root          = None,
                       func          = self.__default_method):
        id = self.get_next_id()
        cmd = c.Command(cmd=command, parent=parentCommand, desc=description, func=func, root=root,identity=id)
        return self.__commands.put_command(cmd = cmd)

    #查看命令行
    def show_command(self):
        print(self.__title.title)
        self.__commands.show_command_tree()

    #执行指令
    def exec_command(self):
        pass

    #get next id
    def get_next_id(self):
        return next(self.__id_iter)