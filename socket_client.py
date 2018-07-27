# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 10:14:49 2018

@author: Vepser
"""

import socket 

client = socket.socket()
client.connect(('localhost',6969))
client.send(b"hello world")
data = client.recv(1024)
print("recv",data)
client.close()
