import requests
from bs4 import BeautifulSoup
import bs4

if __name__ == '__main__':
    def getHTML(url):
        try:
            r=requests.get(url)
            r.raise_for_status()
            r.encoding=r.apparent_encoding
            return r.text
        except:
            return ''
    def fillUni(html,ulist):
        soup=BeautifulSoup(html,"html.parser")
        for i in soup.find('tbody').children :
            if isinstance(i,bs4.element.Tag):
                tsd=i.find_all('td')
                ulist.append([tsd[0].string,tsd[1].string,tsd[3].string])
    def printuni(ulist,num):
        print('{0:^8}\t{1:{3}^20}\t{2:^8}'.format('排名','学校名称','分数',chr(12288)))
        for i in range(num):
            print('{0:^10}\t{1:{3}^20}\t{2:^10}'.format(ulist[i][0],ulist[i][1],ulist[i][2],chr(12288)))
    url='http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    unilist=[]
    html=getHTML(url)
    fillUni(html,unilist)
    num=int(input("请输入想打印的数量："))
    printuni(unilist,num)

