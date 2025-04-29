import socket, time, random, json

SERVER_IP = "127.0.0.1"
PORT = 5000

def get_time():
    return random.randint(int(time.time() - 1e5), int(time.time() + 1e5))

def main():
    server_time = get_time()
    print(f"[SERVER] Time: {server_time} | Listening on {SERVER_IP}:{PORT}")

    server = socket.socket()
    server.bind((SERVER_IP, PORT))
    server.listen()

    clients = []
    while True:
        client, addr = server.accept()
        print(f"[CONNECTED] {addr}")
        clients.append(client)
        if input("Add more clients? (y/n): ").lower() != 'y':
            break

    client_times = []
    for c in clients:
        c.send(json.dumps({"op": "get_time"}).encode())
        data = json.loads(c.recv(1024).decode())
        client_times.append(data["time"])

    avg = (server_time + sum(client_times)) / (len(client_times) + 1)

    for i, c in enumerate(clients):
        offset = avg - client_times[i]
        c.send(json.dumps({"op": "set_time", "offset": offset}).encode())
        print(f"[INFO] Sent offset {offset:.2f} to {c.getpeername()}")

    server.close()

if __name__ == "__main__":
    main()
