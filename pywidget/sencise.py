from numpy import *
class new_win():
    def __init__(self,long,tall):
        self.w = []
        for i in range(0,tall):
            self.w.append([])
            for a in range(0,long):
                self.w[i].append(0)
        self.thing = []
        self.new = 1
    def add(self,name,thing,x,y):
        s[x][y] = self.new
        if thing.type == 's':
            for i in range(thing.x,0 - thing.x):
                for t in range(thing.y,0 - thing.y):
                    self.w[y - i][x - t] = self.new
        self.thing[name] = self.new
        self.new += 1
    def __str__(self):
        return self.w
class new_thing():
    def s(self,x,y):
        self.type = 's'
        self.x = x 
        self.y = y
        return self
