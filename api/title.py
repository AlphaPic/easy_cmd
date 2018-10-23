
class Title:
    def __init__(self):
        self.__version      = 'version 1.0.0'
        self.__author       = 'alan'
        self.__date         = '1970-01-01'
        self.__title        = 'easy cmd' % self.__version

        self.__title_info   = {
            'title'     : self.__title,
            'author'    : self.__author,
            'version'   : self.__version,
            'date'      : self.__date
        }

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __getattr__(self, item):
        print('unknow attributes [ %s ]' % item)

    def _show_title_info(self):
        print(self.__title_info)

    def _set_title(self,title):
        self.__title = title

    def get_attr(self,name):
        return \
                 self.__title if name == 'title' \
            else self.__author if name == 'author' \
            else self.__version if name == 'version' \
            else self.__date if name == 'date' \
            else self.__title_info if name == 'all' \
            else None