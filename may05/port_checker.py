import socket

host = input("Enter host: ")
port = int(input("Enter port: "))

s = socket.socket()
result = s.connect_ex((host, port))

print("Open" if result == 0 else "Closed")
s.close()