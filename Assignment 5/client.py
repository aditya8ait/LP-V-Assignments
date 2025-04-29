import socket, time

ADDR, BUFFER = ("localhost", 8080), 1024

class TokenRingClient:
    def __init__(self):
        self.s = socket.socket()

    def connect(self):
        self.s.connect(ADDR)
        print("Connected to server")

    def start(self):
        try:
            while True:
                data = self.s.recv(BUFFER).decode()
                if data == "TOKEN":
                    print("Token received. Working..."); 
                    time.sleep(5)
                    print("Done. Passing token."); 
                    self.s.send(b"TOKEN")
                elif data == "CLOSE":
                    print("Server closed connection."); 
                    break
        except KeyboardInterrupt:
            print("Interrupted. Closing..."); 
            self.s.send(b"CLOSE")
        finally:
            self.s.close()

if __name__ == "__main__":
    client = TokenRingClient()
    client.connect()
    client.start()
