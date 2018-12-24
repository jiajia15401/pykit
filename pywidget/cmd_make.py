from os import system,popen
import threading
__all__ = ['cmd_run', 'cmd']
global myline
class myline(threading.Thread):   
    def __init__(self, n):
        threading.Thread.__init__(self)
        self.threadID = 11011
        self.name = 'cmd'
        self.counter = 123321
        self.n = n
    def run(self):               
        self.cmd(self.n[0], self.n[1], self.n[2], '(self.if_stop == 1)or(%s)'% self.n[3])
def cmd_run(code,how_print = print):
    try:
        f = os.popen(code)
        how_print(f.read())
    except:
        os.system(code) 
def run_cmd(self,input_thing,how_print,how_input,way_stop):
    self.if_stop = 0
    while True:
        a = how_input(input_thing)
        if (way_stop):
            break
        cmd_run(a, how_print)
myline.cmd = run_cmd
class cmd():
    class cmd(myline):
        pass
    def start(self,input_thing = '>>',how_print = print,how_input = input,way_stop = None):
        n = [input_thing, how_print, how_input, way_stop]
        myline(n)
        myline().start()
        return myline()
    def stop(self):
        self.if_stop = 1
        self.cmd().close()
        self.cmd().join()
if __name__ == '__main__':
    cmd().start()
    __import__('time')
    print('it will stop in 100s')
    time.sleep(100)
    cmd().stop()
    
    
