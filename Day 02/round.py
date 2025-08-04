print("Round Robin CPU Scheduling Algorithm")

n = int(input("Enter number of processes: "))

processes = []
for i in range(n):
    pid = "P" + str(i+1)
    arrival = int(input(f"Enter arrival time for {pid}: "))
    burst = int(input(f"Enter burst time for {pid}: "))
    processes.append([pid, arrival, burst])

time_quantum = int(input("Enter time quantum: "))

remaining = [p[2] for p in processes]
completion = [0] * n
waiting = [0] * n
turnaround = [0] * n
queue = []
current_time = 0
visited = [False] * n
done = 0

while done < n:
    for i in range(n):
        if processes[i][1] <= current_time and not visited[i]:
            queue.append(i)
            visited[i] = True
    if not queue:
        current_time += 1
        continue
    idx = queue.pop(0)
    exec_time = min(time_quantum, remaining[idx])
    current_time += exec_time
    remaining[idx] -= exec_time
    # Add new arrivals during this quantum
    for i in range(n):
        if processes[i][1] > current_time - exec_time and processes[i][1] <= current_time and not visited[i]:
            queue.append(i)
            visited[i] = True
    if remaining[idx] == 0:
        completion[idx] = current_time
        turnaround[idx] = completion[idx] - processes[idx][1]
        waiting[idx] = turnaround[idx] - processes[idx][2]
        done += 1
    else:
        queue.append(idx)

print("\nProcess\tArrival\tBurst\tCompletion\tTAT\tWaiting")
for i in range(n):
    print(f"{processes[i][0]}\t{processes[i][1]}\t{processes[i][2]}\t{completion[i]}\t\t{turnaround[i]}\t{waiting[i]}")

avg_wt = sum(waiting) / n
avg_tat = sum(turnaround) / n
print(f"\nAverage Waiting Time: {avg_wt:.2f}")
print(f"Average Turnaround Time: {avg_tat:.2f}")
