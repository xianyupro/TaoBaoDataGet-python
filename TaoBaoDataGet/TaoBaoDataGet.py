import requests
import re
def getHTMLText(ilt,url):
    try:
        plt=[];
        tlt=[];
        while(plt==[] or tlt==[]):
            r=requests.get(url,timeout=30)
            r.raise_for_status()
            r.encoding=r.apparent_encoding   
            html= r.text
            plt=re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
            tlt=re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price=eval(plt[i].split(':')[1])
            title=eval(tlt[i].split(':')[1])
            ilt.append([price,title])
    except:
        print("")
def  printGoodsList(ilt):
    tplt="{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count=0
    for g in ilt:
        count=count +1
        print(tplt.format(count,g[0],g[1]))
def main():
    goods='会员'
    
    depth=4
    start_url='https://s.taobao.com/search?q='+goods
    infoList=[]
    for i in range(depth):
        try:
            url=start_url+'&s='+str(44*i)
            getHTMLText(infoList,url)
            
        except:
            continue
    printGoodsList(infoList)
main()