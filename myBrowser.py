from tkinter import *
from html.parser import HTMLParser
import urllib.request

class MyHTMLParser(HTMLParser):
    def handle_startag(self,tag,attrs):
        print("Encountered a start tag:",tag)
    def handle_endtag(self,tag):
        print("Encountered a end tag :",tag)
    def handle_data(self,data):
        print("Encountered some data :",data)


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
    parser = MyHTMLParser()
    parser.feed(s)

if __name__ == '__main__':
    main()
