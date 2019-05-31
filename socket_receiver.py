#!/usr/bin/python3
import socket
target_ip="192.168.43.168"
target_port=8888
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((target_ip,target_port))
while True:
    mydata=s.recvfrom(0)
    print(mydata)
    s.senddata("oky got it",mydata[1])

