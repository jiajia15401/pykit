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
    def __init__(self,path = None,class_def = None):
        self.path = path
        self.use = class_def
    def str(self,name,value):
        n = name + '.date'
        if not self.path is None:
            n = self.path + n
        s = open(n,'w')
        v = value
        if not self.use is None:
            s.writelines(self.use(v))
        else:
            s.writelines(use_to_decode.str_to_2(use_to_decode,v))
            s.writelines(use_to_decode.str_to_16(use_to_decode,v))
            s.writelines(hash(v))
