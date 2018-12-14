from os import system,popen
import time
import threading
__all__ = ['cmd_run', 'cmd']
def cmd_run(code,how_print = print()):
    try:
        f = os.popen(code)
        how_print(f.read())
    except:
        os.system(code) 
def run_cmd(self,input_thing,how_print,how_input,way_stop):
    self.if_stop = 0
    while True:
        a = how_input(input_thing)
        if (way_stop)or(self.if_stop == 1):
            break
        cmd_run(a, how_print)
class cmd():
    def __init__(self,input_thing,how_print = print,how_input = input,way_stop = None):
        class myline(threading.Thread):   
            def __init__(self, anser):
                threading.Thread.__init__(self)
                self.threadID = 11011
                self.name = 'cmd'
                self.counter = 123321
                self.anser = anser
            def run(self):               
                n = self.anser
                run_cmd(n[0],n[1] ,n[2],n[3]) 
        cmd = myline([input_thing,how_print,how_input,way_stop])
        cmd.start()
    def stop(self):
        self.if_stop = 1
        cmd.join()
    
