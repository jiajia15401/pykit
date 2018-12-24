__all__ = ['save', 'use_to_decode']
class use_to_decode():
    def str_to_16(self,s):
        return ' '.join([hex(ord(c)).replace('0x', '') for c in s])
    def _16_to_str(self,s):
        return ''.join([chr(i) for i in [int(b, 16) for b in s.split(' ')]])  
    def str_to_2(self,s):
        return ' '.join([bin(ord(c)).replace('0b', '') for c in s])      
    def _2_to_str(self,s):
        return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])
class save():
    
    def __init__(self,path = None,class_ = None,last_name = '.data'):
        self.path = path
        self.use = class_
        self.name = last_name
    def str(self,name,value,last_name = None):
        def str_(self,name,value,last_name = self.name):
            n = name + last_name
            if not self.path is None:
                n = self.path + n
            s = open(n,'w')
            v = value
            if not self.use.str is None:
                s.writelines(self.use().str(v))
            else:
                s.writelines(use_to_decode.str_to_2(use_to_decode,v))
                s.writelines(use_to_decode.str_to_16(use_to_decode,v))
                s.writelines(hash(v))
        if last_name == None:
            str_(name,value)
        else:
            str_(name,value,last_name)
    def list(self,name,value,last_name = None):
        def list_(self,name,value,last_name = '.list' + self.name):
            n = name + last_name
            if not self.path is None:
                n = self.path + n
            s = open(n,'w')
            v = value
            if not self.use.list is None:
                s.writelines(self.use().list(v))
            else:
                for i in v:
                    s.writelines(use_to_decode.str_to_2(use_to_decode,i))
                    s.writelines(use_to_decode.str_to_16(use_to_decode,i))
                    s.writelines(hash(i))
        if last_name == None:
            self.make(name,value)
        else:
            self.make(name,value,last_name)
