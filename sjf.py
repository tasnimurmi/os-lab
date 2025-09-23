
n = int(input("Enter number of processes: "))


pid = []
arrival = []
burst = []



for i in range(n):
    print(f"Process {i+1}:")
    pid.append(f"P{i+1}")
    arrival.append(int(input("  Enter Arrival Time: ")))
    burst.append(int(input("  Enter Burst Time: ")))



ct = [0]*n
tat = [0]*n
wt = [0]*n
completed = [False]*n
current_time = 0
completed_count = 0


while completed_count < n:
    idx = -1
    min_burst = 1000000  # A large number


    
    for i in range(n):
        if arrival[i] <= current_time and not completed[i]:
            if burst[i] < min_burst:
                min_burst = burst[i]
                idx = i
            elif burst[i] == min_burst:  # Tie: Choose one with earlier arrival (optional)
                if arrival[i] < arrival[idx]:
                    idx = i


    if idx == -1:
        current_time += 1  # CPU is idle
        continue


    current_time += burst[idx]
    ct[idx] = current_time
    tat[idx] = ct[idx] - arrival[idx]
    wt[idx] = tat[idx] - burst[idx]
    completed[idx] = True
    completed_count += 1


print("\nPID  AT  BT  CT  TAT  WT")
for i in range(n):
    print(f"{pid[i]}   {arrival[i]}   {burst[i]}   {ct[i]}   {tat[i]}   {wt[i]}")




