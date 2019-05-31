#!/usr/bin/python3
import socket
target_ip="192.168.43.168"
target_port="8888"
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    msg=input("enter your message:-")
    n=msg.encode("ascii")
    s.sendto(n,(target_ip,target_port))
