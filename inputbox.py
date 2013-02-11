from tkinter import *
import urllib.request
class myClient(object):
    def __init__(self):
        self.urlString = 'http://jw2005.scuteo.com/(inh3kz45zvmdtg45zaivog45)/CheckCode.aspx'
        self.localjpg = ""+('checkCode.gif')
        urllib.request.urlretrieve(self.urlString,self.localjpg)
        
        self.top = Tk()
        self.frame = Frame(self.top)
        
        self.fm1 = Frame(self.frame)
        self.userNamelabel = Label(self.fm1,text = '用户名')
        self.userNamelabel.pack(side = LEFT)
        self.userName = Entry(self.fm1)
        self.userName.pack(side = LEFT)
        self.fm1.pack()

        self.fm2 = Frame(self.frame)
        self.userCodelabel = Label(self.fm2,text = '密码   ')
        self.userCodelabel.pack(side = LEFT)
        self.userCode = Entry(self.fm2)
        self.userCode.pack(side = LEFT)
        self.fm2.pack()

        self.fm3 = Frame(self.frame)
        self.checkCodelabel = Label(self.fm3,text = '验证码')
        self.checkCodelabel.pack(side = LEFT)
        self.checkCode = Entry(self.fm3,width = 8)
        self.checkCode.pack(side = LEFT)
        self.image = PhotoImage(file = './checkCode.gif')
        self.C = Canvas(self.fm3,height = 20,width = 60)
        self.C.create_image(35,10,image = self.image)
        self.C.pack(side = LEFT)
        self.fm3.pack()
        
        self.fm4 = Frame(self.frame)
        self.loginButton = Button(self.fm4,text = '登陆',command = self.send)
        self.loginButton.pack(side = LEFT)
        self.quitButton = Button(self.fm4,text = '退出',command = self.top.destroy)
        self.quitButton.pack(side = LEFT)
        #self.imageFile = urllib.request.urlopen(self.urlString)
        self.fm4.pack()

        self.frame.pack()
        
    def send(self):
        print(self.userName.get(),self.userCode.get(),self.checkCode.get())
    
def main():
    d = myClient()
    mainloop()

if __name__ == '__main__':
    main()
