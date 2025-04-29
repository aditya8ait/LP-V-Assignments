class Ring:
    def __init__(self, n=5):
        self.n = n
        self.coordinator = 5
        self.active = set(range(1, n + 1))

    def election(self, pid):
        if self.coordinator is None: self.coordinator = pid; print(f"Process {pid} is the coordinator."); return
        if pid not in self.active: print(f"Process {pid} is not active."); return
        
        highest, next_pid = pid, (pid % self.n) + 1
        while next_pid != pid:
            if next_pid in self.active: 
                print(f"Process {pid} -> Process {next_pid}")
                highest = max(highest, next_pid)
            else: print(f"Process {next_pid} is down.")
            next_pid = (next_pid % self.n) + 1
        self.coordinator = highest
        print(f"Process {self.coordinator} is the coordinator.")

    def start_election(self, pid):
        if pid in self.active: print(f"Process {pid} starts the election."); self.election(pid)
        else: print(f"Process {pid} is not active.")

    def bring_up(self, pid):
        if pid in self.active: print(f"Process {pid} is already up.")
        else: self.active.add(pid); print(f"Process {pid} is up.")

    def bring_down(self, pid):
        if pid not in self.active: print(f"Process {pid} is already down.")
        else:
            self.active.remove(pid); print(f"Process {pid} is down.")
            if self.coordinator == pid: self.start_election(pid)

    def print_active(self): print("Active processes:", *self.active)

    def print_coordinator(self): print(f"Coordinator: Process {self.coordinator}" if self.coordinator else "Coordinator: None")

if __name__ == "__main__":
    ring = Ring()
    while (choice := int(input("\n1) Start Election\n2) Bring Up Process\n3) Bring Down Process\n4) Active Processes\n5) Coordinator\n6) Exit\n")) != 6):
        pid = int(input("Enter process id: "))
        if choice == 1: ring.start_election(pid)
        elif choice == 2: ring.bring_up(pid)
        elif choice == 3: ring.bring_down(pid)
        elif choice == 4: ring.print_active()
        elif choice == 5: ring.print_coordinator()
