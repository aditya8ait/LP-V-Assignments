import socket, time, json, random

SERVER_IP = "127.0.0.1"
PORT = 5000

def get_time():
    return random.randint(int(time.time() - 1e5), int(time.time() + 1e5))

def main():
    sock = socket.socket()
    sock.connect((SERVER_IP, PORT))
    print(f"[CLIENT] Connected to {SERVER_IP}:{PORT}")

    local_time = get_time()

    while True:
        data = json.loads(sock.recv(1024).decode())

        if data["op"] == "get_time":
            print(f"[CLIENT] Time: {local_time}")
            sock.send(json.dumps({"time": local_time}).encode())

        elif data["op"] == "set_time":
            offset = float(data["offset"])
            print(f"[CLIENT] Offset received: {offset}")
            local_time += offset
            print(f"[CLIENT] New time: {local_time}")
            break

    sock.close()

if __name__ == "__main__":
    main()
