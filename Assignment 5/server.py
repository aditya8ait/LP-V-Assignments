# token_ring_server.py
import socket, threading

clients = []

def handle_client(conn, addr, idx):
    while True:
        try:
            data = conn.recv(1024)
            if not data: break
            next_conn = clients[(idx + 1) % len(clients)]
            next_conn.sendall(data)
        except: break
    conn.close()

s = socket.socket()
s.bind(('localhost', 9000))
s.listen(5)

print("Waiting for clients...")
while len(clients) < 3:
    conn, addr = s.accept()
    clients.append(conn)
    print(f"Client {len(clients)} connected")

for i, c in enumerate(clients):
    threading.Thread(target=handle_client, args=(c, None, i)).start()
