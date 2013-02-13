import tkinter as tk
from tkinter.messagebox import showinfo
import urllib.request
import urllib.parse
from html.parser import HTMLParser

class myHTMLParser(HTMLParser):
    flag = 0
    cjUrl = ''
    mainUrl = ''
    tagflag = {'span': 0,'a': 0}
    xmxh = ''
    def handle_starttag(self,tag,attrs):
        if tag == 'span':
            for name,value in attrs:
                if name == 'id':
                    if value == 'xhxm':
                        self.tagflag['span'] = 1
                    if value == 'Label3':
                        self.flag = 1
                        print("登陆成功")
        if tag == 'a':
            self.tagflag['a'] = 1
            for name,value in attrs:
                if name == 'onclick':
                    if value == "GetMc('成绩查询');":
                        self.cjUrl = attrs[0][1]
                        print(value)
                        
    def handle_endtag(self,tag):
        if tag == 'span':
            self.tagflag['span'] = 0
        elif tag == 'a':
            self.tagflag['a'] = 0
    
    def handle_data(self,data):
        if  self.tagflag['span'] == 1:
            self.xmxh = data
            
class myClient(object):
    
    def __init__(self):
        self.root = tk.Frame()
        self.creatWidget()
        self.root.pack()
        
    def creatWidget(self):
        self.hostUrl = 'http://jw2005.scuteo.com/(inh3kz45zvmdtg45zaivog45)/'
        self.urlString = 'http://jw2005.scuteo.com/(inh3kz45zvmdtg45zaivog45)/CheckCode.aspx'
        self.localjpg = ""+('checkCode.gif')
        urllib.request.urlretrieve(self.urlString,self.localjpg)
        
        self.top = tk.Frame(self.root)
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
        self.quitButton = tk.Button(self.top,text = '退出',width = 7,command = self.top.quit)
        self.quitButton.grid(row = 3,column = 2)
        
        self.top.pack()
        
    def send(self):
        datapart1 = '__VIEWSTATE=dDwtMTg3MTM5OTI5MTs7PkfLdDpkwXkZwjVjoRLwfK%2BL%2FuEU&TextBox1='
        datapart2 = '&TextBox2='
        datapart3 = '&TextBox3='
        datapart4 = '&RadioButtonList1=%D1%A7%C9%FA&Button1=&lbLanguage='
        self.body = datapart1+self.userName.get()+datapart2+self.userCode.get()+datapart3+self.checkCode.get()+datapart4
        self.body = self.body.encode('ISO-8859-1')
        self.headers = {'Host':'jw2005.scuteo.com',
                        'Connection':'keep-alive',
                        'Content-Length':len(self.body),
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
        self.req = urllib.request.Request(url = self.loginUrl,data = self.body,headers = self.headers)
        self.data = urllib.request.urlopen(url = self.req).read().decode('gb2312')
        self.myhttpparser = myHTMLParser()
        self.myhttpparser.feed(self.data)
        
        if self.myhttpparser.flag == 1:
            self.xm = self.myhttpparser.xmxh[14:-2]
            self.tempcjUrl = (self.hostUrl+self.myhttpparser.cjUrl)
            pos= self.tempcjUrl.find(self.xm)
            self.cjUrl = self.tempcjUrl[:pos]+urllib.parse.quote(self.tempcjUrl[pos:pos+3].encode('gb2312'))+self.tempcjUrl[pos+3:]
            self.creatWelcomePage()
        else:
            showinfo(title = '切克闹', message = '登陆失败，要么是输错密码要么是验证码要么是账号') 
        
    def creatWelcomePage(self):
        self.fm2 = tk.Frame(self.root)
        self.imformationButton = tk.Button(self.fm2,text = '成绩查询',command = self.checkImformation)
        self.imformationButton.pack()
        self.nameLabel = tk.Label(self.fm2,text = self.xm)
        self.nameLabel.pack()
        self.fm2.pack()
        
    def checkImformation(self):
        header = {'Host': 'jw2005.scuteo.com',
                        'Connection':' keep-alive',
                        'Accept':' text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        'User-Agent':' Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.57 Safari/537.17',
                        'Referer':self.hostUrl+'xs_main.aspx?xh=%s'%self.userName,
                        'Accept-Encoding':' gzip,deflate,sdch',
                        'Accept-Language':' zh-CN,zh;q=0.8',
                        'Accept-Charset':' GBK,utf-8;q=0.7,*;q=0.3',
                        'Cookie':' BIGipServerjwxt_bs_80=1233439198.20480.0000'}
        req = urllib.request.Request(url = self.cjUrl,headers = header)
        self.data = urllib.request.urlopen(url = req).read().decode('gb2312')
        self.creatText()
        
    def creatText(self):
        self.top.destroy()
        self.fm1 = tk.Frame(self.root)
        self.yscrollbar = tk.Scrollbar(self.fm1,orient=tk.VERTICAL)
        self.yscrollbar.pack(side = tk.RIGHT,fill = tk.Y)
        self.xscrollbar = tk.Scrollbar(self.fm1,orient=tk.HORIZONTAL)
        self.xscrollbar.pack(side = tk.BOTTOM,fill = tk.X)
        self.text = tk.Text(self.fm1,
                            yscrollcommand = self.yscrollbar.set,
                            xscrollcommand = self.xscrollbar.set,)
        self.text.insert('end', self.data)
        self.yscrollbar.config(command = self.text.yview)
        self.xscrollbar.config(command = self.text.xview)
        self.text.pack(expand = 'yes')
        self.fm1.pack()
        
        
def main():
    d = myClient()
    tk.mainloop()

if __name__ == '__main__':
    main()

