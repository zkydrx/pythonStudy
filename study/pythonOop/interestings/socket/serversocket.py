# -*- coding: UTF-8 -*-
import socket

# create a socket object
serversocker = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# get local machine name
host =  socket.gethostname()
port =9999
# bind the port
serversocker.bind((host,port))

# queue up to 5 requests
serversocker.listen(5)

while True:
    # establish a connection
    clientsocker,addr = serversocker.accept()
    print('Got a connection from %s'%str(addr))
    msg = 'Got a connection from %s'%str(addr)+'Thank you for connecting'+'\r\n'
    clientsocker.send(msg.encode('utf-8'))
    clientsocker.close()





