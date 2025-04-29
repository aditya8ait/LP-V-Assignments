# 🕒 Berkeley Clock Synchronization – Python Implementation

This project demonstrates the **Berkeley Clock Synchronization Algorithm** using a simple **client-server model** in Python. It simulates multiple machines (clients) each having an unsynchronized local clock. A central server collects the local times, calculates a correction offset, and sends it back to the clients to align their clocks.

---

## 📁 Files

- `server.py` – Time coordinator (server).
- `client.py` – Simulated client with a local clock.

---

## ⚙️ Requirements

- Python 3.x
- Visual Studio Code (VS Code) or any Python-compatible IDE
- No external libraries required

---

## 🚀 How to Run the Project


### 1. **Open in VS Code**

- Open the folder in Visual Studio Code.
- Make sure Python is installed and configured in VS Code.

### 2. **Open Multiple Terminals**

- Go to **Terminal → New Terminal**.
- Open **at least two terminals**:
  - One for the **server**
  - One or more for **clients**

### 3. **Run the Server**

In the first terminal, run:

```bash
python Server.py

```
### 4. **Run the Client**

In the first terminal, run:

```bash
python Client.py
