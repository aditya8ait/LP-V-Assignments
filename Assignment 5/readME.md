# 🧿 Token Ring Algorithm in Python (Client-Server Simulation)

This is a simple implementation of the **Token Ring Algorithm** using Python sockets with a central server and multiple clients (nodes). The server handles message passing between clients in a ring topology. Clients take turns accessing a simulated critical section by passing a token.

---

## 📁 Files

- `server.py` — Central server that routes the token between clients.
- `client.py` — Clients that receive, hold, and pass the token.

---

## ⚙️ Requirements

- Python 3.x
- OS: Linux, macOS, or Windows
- Works locally using `localhost` on port `9000`

---

## 🚀 How to Run

### 1. **Start the Server**

Open a terminal and run:

```bash
python token_ring_server.py
```
###2. **Start clients**
```bash
python client.py 0
python client.py 1
python client.py 2
