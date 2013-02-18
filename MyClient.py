'''
Created on 2013-2-18

@author: unhealthy
'''
import BrowerserWidget
import LoginWidget
import threading
import tkinter as tk

class MyThread(threading.Thread):
    def __init__(self,func,args,name = ''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name
    
    def run(self):
        self.res = self.func(*self.args)
    
    def getResponse(self):
        return self.res
    
def main():
    e = threading.Event()
    l = LoginWidget.loginWidget(event = e)
    b = BrowerserWidget.browerserWidget(event = e,loginW = l)
    t2 = threading.Thread(target = b.creatMainWindow,args = ())
    t2.start()
    tk.mainloop()

if __name__ == '__main__':
    main()