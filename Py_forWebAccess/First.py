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
gettingHTTPEng()



