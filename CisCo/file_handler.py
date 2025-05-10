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

    
