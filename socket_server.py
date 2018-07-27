# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 10:25:31 2018

@author: Vepser
"""

import socket

server = socket.socket()
server.bind(('localhost',6969)) #綁定要監聽端口
server.listen() #端口
print("start waitting")
conn,addr = server.accept() #等待 返回一實例 及 地址
print(conn,addr)

data = conn.recv(1024)
print("recv:",data)
conn.send(data.upper())

server.close()