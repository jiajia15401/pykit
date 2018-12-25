class new_win():
    def __init__(self,long,tall):
        self.w = []
        for i in range(0,tall):
            self.w.append([])
            for a in range(0,long):
                self.w[i].append(0)
        self.thing = []
        self.new = 1
        self.touch = []
        self.touch_thing = []
        self.name = {}
        self.touch_name = []
        self.big = []
        
    def add(self,thing,x,y):
        self.thing.append(thing())
        s[x][y] = self.new
        self.name[self.new] = thing().name 
        if thing.type == 's':
            for i in range(thing.x,0 - thing.x):
                for t in range(thing.y,0 - thing.y):
                    if self.w[y-i][x -t] == 0:
                        self.w[y - i][x - t] = self.new
                    else:
                        self.touch.append([x-i,y-t])
                        self.touch_name.append([thing.name(),self.name[s[x-i,y-t]]])
        self.big.append(x*y)
    def if_touch(self,x,y):
        n = [x,y]
        for i in self.touch:
            if i[0] == n[0]:
                if i[1] == n[1]:
                    return true
    def when_touch(self,onename,twoname):
        self.thing[name] = self.new
        self.new += 1
        while True:
            for u in self.touch_name:
                if (u[0] == onename):
                   if u[1] == twoname:
                       break 
                if (u[1] == onename):
                    if u[0] == twoname:
                        break
    def __str__(self):
        return self.w
    def show(self):
        pass
class new_thing():
    def __init__(self,x,y,name):
        self.type = 's'
        self.x = x 
        self.y = y
        self.name = name
    def __str__(self):
        return self.name
if __name__ == '__main__':
    win = new_win(100,100)
    
