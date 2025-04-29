import random

class Bully:
    def __init__(self, n=5):
        self.n = n
        self.up = [True] * n
        self.leader = n

    def election(self, pid):
        print(f"Process {pid} starts election")
        for i in range(pid, self.n + 1):
            if self.up[i - 1]: cod = i; 
            print(f"  → Election msg to process {i}")
        self.leader = cod
        print(f"Process {cod} becomes coordinator")

    def set_up(self, pid):
        if self.up[pid - 1]: print(f"Process {pid} already up")
        else: self.up[pid - 1] = True; print(f"Process {pid} is up"); self.election(pid)

    def set_down(self, pid):
        if not self.up[pid - 1]: print(f"Process {pid} already down")
        else:
            self.up[pid - 1] = False
            print(f"Process {pid} is down")
            if self.leader == pid:
                alive = [i + 1 for i, p in enumerate(self.up) if p]
                self.election(random.choice(alive))

    def message(self, pid):
        if not self.up[pid - 1]: print(f"Process {pid} is down")
        elif self.up[self.leader - 1]: print("OK")
        else: self.election(pid)

if __name__ == "__main__":
    b = Bully()
    print("Processes up: p1 p2 p3 p4 p5")
    print(f"Process {b.leader} is coordinator")

    while True:
        print("\n1) Up\n2) Down\n3) Message\n4) Exit")
        c = int(input("Enter choice: "))
        if c == 4: break
        pid = int(input("Enter process ID: "))
        if c == 1: b.set_up(pid)
        elif c == 2: b.set_down(pid)
        elif c == 3: b.message(pid)
