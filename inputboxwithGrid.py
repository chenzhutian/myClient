import tkinter as tk
import urllib.request


class myClient(object):
    def __init__(self):
        self.urlString = 'http://jw2005.scuteo.com/(inh3kz45zvmdtg45zaivog45)/CheckCode.aspx'
        self.localjpg = ""+('checkCode.gif')
        urllib.request.urlretrieve(self.urlString,self.localjpg)
        
        self.top = tk.Tk()
        
        self.userNamelabel = tk.Label(self.top,text = '用户名')
        self.userNamelabel.grid(row = 0,column = 0)
        self.userName = tk.Entry(self.top)
        self.userName.grid(row = 0,column = 1,columnspan = 2)

        self.userCodelabel = tk.Label(self.top,text = '密码   ')
        self.userCodelabel.grid(row = 1,column = 0)
        self.userCode = tk.Entry(self.top)
        self.userCode.grid(row = 1,column = 1,columnspan = 2)
        
        self.checkCodelabel = tk.Label(self.top,text = '验证码')
        self.checkCodelabel.grid(row = 2,column = 0)
        self.checkCode = tk.Entry(self.top,width = 8)
        self.checkCode.grid(row = 2,column = 1,ipadx = 10)
        self.image = tk.PhotoImage(file = './checkCode.gif')
        self.C = tk.Canvas(self.top,height = 20,width = 60)
        self.C.create_image(35,10,image = self.image)
        self.C.grid(row = 2,column = 2)

        self.loginButton = tk.Button(self.top,text = '登陆',width = 7,command = self.send)
        self.loginButton.grid(row = 3,column = 1)
        self.quitButton = tk.Button(self.top,text = '退出',width = 7,command = self.top.destroy)
        self.quitButton.grid(row = 3,column = 2)
        #self.imageFile = urllib.request.urlopen(self.urlString)
        
        
    def send(self):
        datapart1 = '__VIEWSTATE=dDwtMTg3MTM5OTI5MTs7PkfLdDpkwXkZwjVjoRLwfK%2BL%2FuEU&TextBox1='
        datapart2 = '&TextBox2='
        datapart3 = '&TextBox3='
        datapart4 = '&RadioButtonList1=%D1%A7%C9%FA&Button1=&lbLanguage='
        self.data = datapart1+self.userName.get()+datapart2+self.userCode.get()+datapart3+self.checkCode.get()+datapart4
        self.data = self.data.encode('ISO-8859-1')
        self.headers = {'Host':'jw2005.scuteo.com',
                        'Connection':'keep-alive',
                        'Content-Length':len(self.data),
                        'Cache-Control':'max-age=0',
                        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        'Origin':'http://jw2005.scuteo.com',
                        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.57 Safari/537.17',
                        'Content-Type':'application/x-www-form-urlencoded',
                        'Referer':'http://jw2005.scuteo.com/(inh3kz45zvmdtg45zaivog45)/default2.aspx',
                        'Accept-Encoding':'gzip,deflate,sdch',
                        'Accept-Language':'zh-CN,zh;q=0.8',
                        'Accept-Chaset':'GBK,utf-8;q=0.7,*;q=0.3',                       
                        'Cookie':'BIGipServerjwxt_bs_80=1233439198.20480.0000'}
        self.loginUrl = 'http://jw2005.scuteo.com/(inh3kz45zvmdtg45zaivog45)/default2.aspx'
        self.req = urllib.request.Request(url = self.loginUrl,data = self.data,headers = self.headers)
        s = urllib.request.urlopen(url = self.req).read().decode('gb2312')
        
        self.subtop = tk.Tk()
        self.fm1 = tk.Frame(self.subtop)
        self.yscrollbar = tk.Scrollbar(self.fm1,orient=tk.VERTICAL)
        self.yscrollbar.pack(side = tk.RIGHT,fill = tk.Y)
        self.xscrollbar = tk.Scrollbar(self.fm1,orient=tk.HORIZONTAL)
        self.xscrollbar.pack(side = tk.BOTTOM,fill = tk.X)
        self.text = tk.Text(self.fm1,yscrollcommand = self.yscrollbar.set,
                            xscrollcommand = self.xscrollbar.set,)
        self.text.insert('end', s)
        self.yscrollbar.config(command = self.text.yview)
        self.xscrollbar.config(command = self.text.xview)
        self.text.pack()
        self.fm1.pack()
        
        
def main():
    d = myClient()
    tk.mainloop()

if __name__ == '__main__':
    main()



















    
