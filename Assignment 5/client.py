# token_ring_client.py
import socket, time, sys

id = sys.argv[1]

s = socket.socket()
s.connect(('localhost', 9000))

if id == '0':  # only client 0 starts with the token
    time.sleep(1)
    s.sendall(b"TOKEN")

while True:
    token = s.recv(1024)
    if token:
        print(f"Client {id} has token")
        time.sleep(1)  # simulate critical section
        s.sendall(token)
