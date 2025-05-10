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
    
