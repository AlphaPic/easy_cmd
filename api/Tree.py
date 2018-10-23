
class TreeNode:
    def __init__(self,cmd=None):
        self._root_cmd      = cmd
        self._child_cmd     = []

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __enter__(self):
        return self