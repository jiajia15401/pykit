from pywidget.decode import decode
class load():
    def __init__(self,path = None,class_def = None,last_name = '.data'):
        self.path = path
        self.use = class_def
        self.name = last_name
    def str(self,name,last_name = None):
        def str_(self,name,last_name = self.name):
            n = name + self.name
            if not self.path is None:
                n = self.path + n
            s = open(n,'r')
            if not self.use() is None:
                self.use().str(s)
            else:
                n = decode()._2_to_str(s.readline())
                if n == decode()._16_to_str(s.readline()):
                    if hash(n) == s.readline():
                        return n
                else:
                    return "can't find %s" % name
        if last_name == None:
            return str_(name,value)
        else:
            return str_(name,value,last_name)
    def list(self,name,last_name = None):
        def list_(self,name,last_name = '.list' + self.name):
            n = name + last_name
            if not self.path is None:
                n = self.path + n
            s = open(n,'r')
            if not self.use() is None:
                n = self.use().list(s)
            else:
                l = []
                while True:
                    n = decode()._2_to_str(s.readline())
                    if n == decode()._16_to_str(s.readline()):
                        if hash(n) == s.readline():
                            l.append(n)
                    else:
                        break
            return n
        if last_name == None:
            return list_(name,value)
        else:
            return list_(name,value,last_name) 
    
