# Echo client program
import socket

HOST = '128.6.13.155'    # The remote host
PORT = 50007              # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket has been created'
s.connect((HOST, PORT))
print 'Socket has connected'
s.send('Hello, world')
print 'Sent message'
data = s.recv(1024)
print 'about to close socket'
s.close()
print 'Received', repr(data)
