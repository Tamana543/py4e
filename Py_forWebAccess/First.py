

print("This is Tamana Farzami ,and I am happy to see you all here :)")

print("This is Tamana Farzami ,and I am happy to see you all here :)")

import re
file = open('RegexCheetsheet')
for line in file:
    line = line.rstrip()
    if re.search('^{',line):
        print(line)