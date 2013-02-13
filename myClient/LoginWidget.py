'''
Created on 2013-2-13
Login Widget
@author: unhealthy
'''
import tkinter as tk
import tkinter.messagebox
import urllib.request
import urllib.parse
from html.parser import HTMLParser

class loginWidget(object):
    class LoginParser(HTMLParser):
        pass
    
    userName = ''
    userCode = ''
    userCookie = ''
    checkCode = ''
    mianUrl = ''
    xm = ''
    checkCodePath = 'CheckCode.aspx'
    loginPath = 'default2.aspx'
    loginParser = LoginParser()
    loginState = False
    
    def __init__(self):
        f = urllib.request.urlopen('http://jw2005.scuteo.com/')
        p = (urllib.parse.urlparse(f.geturl()))[2]
        self.mainUrl = 'http://jw2005.scuteo.com/'+ p[1:p.rfind('/')+1]
        Cookie = f.info()['Set-Cookie']
        self.userCookie = Cookie[:Cookie.find(';')]
        self.root = tk.Tk()
        self.creatWidget()
        
    def creatWidget(self):
        localjpg = ""+('checkCode.gif')
        urllib.request.urlretrieve(self.mainUrl+self.checkCodePath,localjpg)
        
        self.loginFrame = tk.Frame(self.root)
        self.loginFrame.pack()
        
        self.userNamelabel = tk.Label(self.loginFrame,text = '用户名')
        self.userNamelabel.grid(row = 0,column = 0,sticky = tk.W)
        self.userNameEntry = tk.Entry(self.loginFrame)
        self.userNameEntry.grid(row = 0,column = 1,columnspan = 2,sticky = tk.E)

        self.userCodelabel = tk.Label(self.loginFrame,text = '密码')
        self.userCodelabel.grid(row = 1,column = 0,sticky = tk.W)
        self.userCodeEntry = tk.Entry(self.loginFrame)
        self.userCodeEntry.grid(row = 1,column = 1,columnspan = 2,sticky = tk.E)
        
        self.checkCodelabel = tk.Label(self.loginFrame,text = '验证码')
        self.checkCodelabel.grid(row = 2,column = 0,sticky = tk.W)
        self.checkCodeEntry = tk.Entry(self.loginFrame,width = 8)
        self.checkCodeEntry.grid(row = 2,column = 1,ipadx = 10,sticky = tk.E)
        self.image = tk.PhotoImage(file = './checkCode.gif')
        self.C = tk.Canvas(self.loginFrame,height = 20,width = 60)
        self.C.create_image(35,10,image = self.image)
        self.C.grid(row = 2,column = 2,sticky = tk.E)

        self.loginButton = tk.Button(self.loginFrame,text = '登陆',width = 7,command = self.login)
        self.loginButton.grid(row = 3,column = 1)
        self.quitButton = tk.Button(self.loginFrame,text = '退出',width = 7,command = self.root.destroy)
        self.quitButton.grid(row = 3,column = 2)
        
    def login(self):
        if len(self.userNameEntry.get()) != 12:
            tkinter.messagebox.showwarning('错误', '用户名长度不对')
        elif len(self.checkCodeEntry.get()) != 5:
            tkinter.messagebox.showwarning('错误', '验证码不正确')

def main():
    loginWidget()
    tk.mainloop()

if __name__ == '__main__':
    main()
    
    
