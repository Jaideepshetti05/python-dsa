import socket

target = "127.0.0.1"

for port in range(20, 30):
    s = socket.socket()
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is open")
    s.close()