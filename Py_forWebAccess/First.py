import re


def practice():
    file = open('RegexCheetsheet')
    for line in file:
        line = line.rstrip()
        if re.search('^{',line):
            print(line)
 
# Regex Practice 
def assissmentData():
    item_sum = 0
    print("Start")
    data = open("data.txt")
    for line in data :
        line = line.strip()
        
        first = re.findall('[0-9]+',line)
        # print(first)
        # stringNum = ''.join(first)
        for item in first:
            
            Numbers = int(item)
            item_sum +=Numbers 
            # Numbers += Numbers
        
    print(item_sum)

# assissmentData()
#  Get the Socket and use it for extracting websites data 😉
import socket 
def gettingHTTPEng():
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org',80))
    cmd =  'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)

    while True :
        data = mysock.recv(512)
        if (len(data) < 1 ) :
            break
        print(data.decode())
    mysock.close() 
# gettingHTTPEng()

# Or You can use this trick 
import urllib.request, urllib.parse , urllib.error
def gettingHTTPEng_() :

    fhand = urllib.request.urlopen('https://en.wikipedia.org/wiki/Lorem_ipsum')
    for line in fhand :
     print(line.decode().strip())

# gettingHTTPEng_()

# To Count a WEbsite words 
def web_words_counter() : 
    fhand = urllib.request.urlopen('http://data.pr4e.org/intro-short.txt')
    counts = dict()
    for line in fhand:
        words = line.decode().split()
        for word in words :
            counts[word] = counts.get(word,0) + 1
    print(counts)
# web_words_counter()

from bs4 import BeautifulSoup
import ssl
# to ignore SSL certificate errors 

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def linksOuter() :
    file = input("File URL : ")
    html = urllib.request.urlopen(file,context=ctx).read()
    data = BeautifulSoup(html , 'html.parser')
    tags = data('img')
    for tag in tags :
        print(tag.get('src' ,None))
linksOuter()

def Assignment4_3() :
    sumNum = 0
    file = input("File URL : ")
    html_data = urllib.request.urlopen(file,context=ctx)
    data = BeautifulSoup(html_data,'html.parser')
    # tags = data("span")
    tags = data.find_all('span')
    for tag in tags :
        span_data = tag.get_text()
        span_data_Num = int(span_data)
        sumNum += span_data_Num
    print(sumNum)
# Assignment4_3()

def Assignment4_4() :
   
    position = 18 
    count = 7
    dictionary = []
    file = input("File URL : ")
    html_data = urllib.request.urlopen(file,context=ctx)
    data = BeautifulSoup(html_data,'html.parser')
    tags = data.find_all("a")
    for _ in range(count): 
        a_links= tags[position - 1].get("href",None)
        name = a_links.split("_")[-1].split(".")[0]  
        # dictionary.append(a_links) 
    print("Last name in sequence:", name)
# Assignment4_4()

#  XML in Python Practuice
import xml.etree.ElementTree as Ex
def XMLPractice() : 
    data = '''
    <person>
    <name>Tamana Farzami</name>
    <phone type="intl">+93 782177966 </phone>

    <email hide="yes"/>
    </person>
    '''
    tree = Ex.fromstring(data)
    print("Name : ", tree.find('name').text)
    print("phone : ",tree.find("phone").text)
    print("Email : ", tree.find("email").get("hide"))

# XMLPractice()
# Assignment ExtractingData
def assigmentExtr() : 
    counter = 0
    item_list = list()
    link = input("Enter the URL: ")
    XML_data = urllib.request.urlopen(link)
    data = XML_data.read()
    tree = Ex.fromstring(data)
    main_data = tree.findall('.//count')
    for item in main_data :
        # item_num = int(item)
        item_list.append(item.text)
        # counter += item_num
    print(item_list)

assigmentExtr()



