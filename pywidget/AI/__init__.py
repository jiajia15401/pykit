__all__ = ['ai']
v = '1.0.0'
class ai():
    def make(self,path):
        n = path + '.py'
        self.name = n
        s = open(n ,'w')
        run = '''class ai():
    name = "%s"
    def __init__(self):
        self.list = []
        self.add = []
    def why(self):
        pass
    def think(self):
        self.why()
    def work(self):
        now = []
        while True:
            for i in self.add
                i()
                now.append('%s 1' % i)
                for o in self.goal:
                    if not o():
                        list_of_goal("%s %s0" % now o)
            list_of_goal("%s 1" % now)
            self.think()
    def add(self,add):
        self.add.append(add)
    def list_of_goal(self,goal):
        self.list.append(goal)
'''% name
        s.writelines (run)
        return ai()
