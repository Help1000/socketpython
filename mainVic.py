from cgitb import reset
import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

c.connect(("181.45.117.98", 8000))

while True:
    mensaje = input("Su mensaje> ")
    c.send(mensaje.encode("utf-8"))
    print(c.recv(1080).decode("utf-8"))