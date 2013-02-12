import tkinter as tk
from html.parser import HTMLParser
from html.entities import name2codepoint
import urllib.request


class myHTMLParser(HTMLParser):
    def __init__(self,data = 'default'):
        HTMLParser.__init__(self)
        self.top = tk.Tk()
        self.s = tk.StringVar(self.top)
        
        #self.label = tk.Label(self.top,text = self.s)
        self.fm1 = tk.Frame(self.top)
        
        self.yscrollbar = tk.Scrollbar(self.fm1)
        self.yscrollbar.pack(side = tk.RIGHT,fill = tk.Y)
        self.xscrollbar = tk.Scrollbar(self.fm1)
        self.xscrollbar.pack(side = tk.BOTTOM,fill = tk.X)
        self.text = tk.Text(self.fm1,yscrollcommand = self.yscrollbar.set,
                            xscrollcommand = self.xscrollbar.set)
        self.text.insert('end', data)
        self.yscrollbar.config(command = self.text.yview)
        self.xscrollbar.config(command = self.text.xview)
        self.text.pack()
        self.fm1.pack()
        self.s.set(data)
    
    def handle_startag(self,tag,attrs):
        self.label.config(text = tag)
    def handle_endtag(self,tag):
        self.s.set("End tag :"+tag)
    def handle_data(self,data):
        print("Data  :",data)
    def handle_comment(self,data):
        self.s.set("Comment :"+data)
    def handle_entityref(self,name):
        c = chr(name2codepoint[name])
        self.s.set("Named ent:"+c)
    def handle_charref(self,name):
        if name.startswith('x'):
            c = chr(int(name[1:],16))
        else:
            c = chr(int(name))
        self.s.set("Num ent :"+c)
    def handle_decl(self,data):
        self.s.set("Decl      :"+data)

    
    
def main():
    data ='__VIEWSTATE=dDwtMTg3MTM5OTI5MTs7PkfLdDpkwXkZwjVjoRLwfK%2BL%2FuEU&TextBox1=201130630338&TextBox2=230059&TextBox3=48814&RadioButtonList1=%D1%A7%C9%FA&Button1=&lbLanguage='
    data =data.encode('ISO-8859-1')
    headers = {'Host':'jw2005.scuteo.com',
               'Connection':'keep-alive',
                    'Content-Length':len(data),
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
    loginUrl = 'http://jw2005.scuteo.com/(inh3kz45zvmdtg45zaivog45)/default2.aspx'
    req = urllib.request.Request(url = loginUrl,data = data,headers = headers)
    s = urllib.request.urlopen(url = req).read().decode('gb2312')
    print(s)
    browser = myHTMLParser(data = s)
    tk.mainloop()
    
if __name__ == '__main__':
    main()
