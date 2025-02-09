import re


def practice():
    file = open('RegexCheetsheet')
    for line in file:
        line = line.rstrip()
        if re.search('^{',line):
            print(line)
 
# Regex Practice 
def assissmentData():
    print("Start")
    data = open("data.txt")
    for line in data :
        line = line.strip()
        if re.search('[0-9]+',line):
            first = re.findall('[0-9]+',line)
            stringNum = ''.join(first)
            Numbers = int(stringNum)
            print(Numbers)

assissmentData()


