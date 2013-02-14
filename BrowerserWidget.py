'''
Created on 2013-2-14
BrowerserWidget
@author: unhealthy
'''

import tkinter as tk
import urllib.request
from html.parser import HTMLParser
import LoginWidget
import MenuPath

class CjParser(HTMLParser):
    pass

class browerserWidget(object):
    userName = ''
    userCode = ''
    userCookie = ''
    mainUrl = ''
    userXm = ''
    mainPath = ''
    loginState = False
    menuPath = MenuPath.MenuPath()

    def __init__(self,loginW):
        self.userName = loginW.userName
        self.userCode = loginW.userCode
        self.userCookie = loginW.userCookie
        self.mainUrl = loginW.mainUrl
        self.mainPath = loginW.mainPath
        self.menuPath = loginW.menuPath
        self.creatMainWindow()
        
    def creatMainWindow(self):
        self.MainWindow = tk.Tk()
        self.MainWindow.minsize(160*6, 90*6)
        self.MainWindow.maxsize(160*6, 90*6)
        self.menuBar = tk.Menu(self.MainWindow)
        self.MainWindow.config(menu = self.menuBar)
        self.menuBar.add_command(label = '查询成绩',command = self.creatCjWidget)
        self.menuBar.add_command(label = '选课',command = self.creatXkWidget)

    def creatCjWidget(self):
        self.cjFrame = tk.Frame(self.MainWindow,height = 90*6,width = 160*6)
        self.cjFrame.grid(column=0, row=0)
        
        cjLabelFrame1 = tk.LabelFrame(self.cjFrame,height = 90,width = 160*6-1)
        cjLabelFrame2 = tk.LabelFrame(self.cjFrame,height = 90*5, width = 160*6-1)
        
        cjLabelFrame1.grid(column = 0,row = 0,columnspan = 16,rowspan = 2)
        cjLabelFrame2.grid(column = 0,row = 2,columnspan = 16,rowspan = 5)
        
    def creatXkWidget(self):
        self.cjFrame.destroy()
def main():
    browerserWidget(LoginWidget.loginWidget())
    tk.mainloop()

if __name__ == '__main__':
    main()
    