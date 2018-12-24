import threading
class new_line(threading.Thread):
    def __init__(self, ID = 8080,name = 'new_line', counter = 101010):
        threading.Thread.__init__(self)
        self.threadID = ID
        self.name = name
        self.counter = counter
    def run(self):
        self.code()
    def end(self):
        self.john()
class def_line():
    def __init__(self,def_,dpass):
        t= threading.Thread(target=def_,args=dpass)
        self.t = t
        self.t().start()
    def end(self,stop_time=0):
        self.t.john(stop_time)
    
        
