from pywidget.decode import decode
class load():
    def __init__(self,path = None,class_def = None):
        self.path = path
        self.use = class_def
    def str(self,name):
        n = name + '.date'
        if not self.path is None:
            n = self.path + n
        s = open(n,'r')
        if not self.use() is None:
            self.use(s)
        else:
            n = decode()._2_to_str(s.readline())
            if n == decode()._16_to_str(s.readline()):
                if hash(n) == s.readline():
                    return n
            else:
                return 'can find %s' % name
