import errno
from os import strerror
try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # Actual processing goes here.
    s.close()
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("The file doesn't exist.")
    elif exc.errno == errno.EMFILE:
        print("You've opened too many files.")
    else:
        print("The error number is:", exc.errno)
#or
try :
    s = open("file","rt")
     # the codes functionality 
    s.close()
except Exception as exc :
     print("The file could not be opened:", strerror(exc.errno)) # the sterror expects just one argument – an error number

try:
    counter = 0
    stream = open('text.txt', "rt")
    char = stream.read(1)
    while char != '':
        print(char, end='')
        counter += 1
        char = stream.read(1)
    stream.close()
    print("\n\nCharacters in file:", counter)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
print("next ")
try:
    ccnt = lcnt = 0
    s = open('text.txt', 'rt')
    lines = s.readlines(20)
    while len(lines) != 0:
        for line in lines:
            lcnt += 1
            for ch in line:
                print(ch, end='')
                ccnt += 1
        lines = s.readlines(10)
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

print("Write Methood ")
try:
    file = open('file.txt','wt')
    for item in range(10):
        file.write("line #" + str(item + 1) + "\n")
    file.close()
except IOError as e :
     print("I/O error occurred: ", strerror(e.errno))

# Handling Bytearrays 
data = bytearray(10)
for i in range(len(data)):
    data[i] = 10-i 
for b in data :
    print(hex(b))

# Readint : to read data from Binarry file 
data = bytearray(10)
try :
    binary_file = open('textfile.txt','rb')
    binary_file.readinto(data)
    binary_file.close()
    for byte in data:
        print(hex(byte),end=" ")
except IOError as error :
    print("I/O error occured :" , strerror(error.errno))

# or the same task by using read() : Be careful – don't use this kind of read if you're not sure whether the file's contents will fit the available memory.
try:
    binary_file = open('file.bin', 'rb')
    data = bytearray(binary_file.read())
    binary_file.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

    
# A file hundler complete applicataion 
srcname = input("Enter the source file name :")
try :
    src = open(srcname, "rb")
except IOError as error :
    print("Cannot open the source file: ", strerror(error.errno))
    exit(error.errno)

dstname  = input("Enter the destination file name :")
try: 
    dst = open(dstname, 'wb')
except Exception as error :
    print("Cannot create the destination file: ", strerror(error.errno))
    src.close()
    exit(error.errno)

buffer = bytearray(65536)
total =0 
try :
    readin = src.readinto(buffer)
    while readin > 0 :
        written = dst.write(buffer[:readin])
        total += written
        readin = src.readinto(buffer)
except IOError as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    exit(e.errno)	

print(total,'byte(s) successfully written')
src.close()
dst.close()

# Some mini apps ------

#  character frequency histogram
counters = {chr(ch) : 0 for ch in range(ord('a'),ord('z') + 1)}
file_name = input("Enter the name of the file to analyze : ")
try :
    file = open(file_name , 'rt')
    for line in file :
        for char in line :
            # the letter
            if char.isalpha():
                counters[char.lower()] +=1
    file.close()

    # output 
    for char in counters.keys():
        c = counters[char]
        if c > 0 :
            print(char,'->',c)
except IOError as error :
    print("I/O error occirred :" , strerror(error.errno))

# Sorted Character Frequency histogram 
counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
file_name = input("Enter the name of the file to analyze: ")
try:
    file = open(file_name, "rt")
    for line in file:
        for char in line:
            if char.isalpha():
                counters[char.lower()] += 1
    file.close()
    file = open(file_name + '.hist', 'wt')
    # use a lambda to access the directory's elements and set reverse to get a valid order.
    for char in sorted(counters.keys(), key=lambda x: counters[x], reverse=True):
        c = counters[char]
        if c > 0:
            file.write(char + ' -> ' + str(c) + '\n')
    file.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))

# Evaluating Student Result ( complete App ) 
class  StudentDataException(Exception) :
    pass

class WrongLine(StudentDataException):
    def __init__(self, line_number, line_string):
        super().__init__(self)
        self.line_number = line_number
        self.line_string = line_string
     
#empty file 
class FileEmpty(StudentDataException) :
    def __init__(self):
        super().__init__(self) 

# student data dic 
data = {}    