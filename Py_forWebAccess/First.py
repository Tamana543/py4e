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

assissmentData()


