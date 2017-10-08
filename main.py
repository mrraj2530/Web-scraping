from BeautifulSoup import *
import requests
import re
headers={'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'}
games=open('sports.txt','r').read().split('\n')
filename=raw_input("Enter filename:")
try:
    fh=open(filename,'r')
except:
    print "%s not exist " %filename
    exit()
for url in fh:
    flag=0
    if url=='\n':
        continue
    url=url.rstrip()
    if not (url.startswith("http://") or url.startswith("https://")):
        url="http://"+url
    print url
    try:
        r=requests.get(url,headers=headers)
        if r.status_code==404:
            print "Invalid Webpage"
            continue
    except:
	    print "Invalid URL"
	    continue
    soup=BeautifulSoup(r.text)
    title=soup('title')
    title=str(title).lower()
    meta=soup('meta')
    script=soup('script')
    for sport in sports:
        if re.search(sport,title):
            print sport
            flag=1
            break
    if flag!=1:
        for sport in sports:
            if re.search(sport,str(meta)):
                flag=1
                print sport
                break
    if flag!=1:
        for sport in sports:
            if re.search(sport,str(script)):
                flag=1
                print sport
                break
    if flag!=1:
        print "N/A"
fh.close()