#Client side

import socket
s=socket.socket()
port=12345
host=socket.gethostname()
s.connect((host,port))
print("The message received from server is ",s.recv(1024))
s.close()

#Server side

import socket
s=socket.socket()
print("Socket successfully created")
port = 12345
host=socket.gethostname()
s.bind((host,port))
print("Socket binded to",port)
s.listen(5)
print("Socket is listening")
while True:
    c,addr=s.accept()
    print("Got connection from ",addr)
    out="Thank you for Connecting"
    c.sendall(out.encode('utf-8'))
    c.close()
