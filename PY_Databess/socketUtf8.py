import socket
 
mysock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
mysock.connect(('data-pr4e.org',80))
cmd = 'GET  '.encode() # add link after GET
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1) :
        break
    print(data.decode())
mysock.close()