import socket
import os
import time

TCP_IP = '104.236.69.2'
TCP_PORT = 21225

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("gmail.com",80))
ip = s.getsockname()[0]
print(ip)
s.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TCP_IP, TCP_PORT))

sock.send(b"True")
time.sleep(0.1)
sock.send(str(ip).encode())

sock.close()

mjpg_streamer = input("mjpg_streamer root : ")
cam = input("Device : ")

stream = "./mjpg_streamer -i \"./input_uvc.so -d /dev/video" + cam + " -y\" -o \"./output_http.so -w ./www\""

os.chdir(mjpg_streamer)
os.system(stream)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TCP_IP, TCP_PORT))

sock.send(b"False")
time.sleep(0.1)
sock.send(b"0.0.0.0")

sock.close()

print("Thank you for using this script")