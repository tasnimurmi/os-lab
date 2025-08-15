



n = int(input("Number of processes: "))
proc = []
for i in range(n):
    pid = input(f"PID {i+1}: ").strip() or str(i+1)
    at = int(input("  AT: "))
    bt = int(input("  BT: "))
    pr = int(input("  Priority: "))
    proc.append({'pid': pid, 'at': at, 'bt': bt, 'pr': pr, 'idx': i, 'done': False})


time = min(p['at'] for p in proc)  
done = 0
while done < n:
    ready = [p for p in proc if p['at'] <= time and not p['done']]
    if not ready:
        time = min(p['at'] for p in proc if not p['done'])
        continue
    cur = min(ready, key=lambda x: (x['pr'], x['at'], x['idx']))
    cur['ct']  = time
    cur['tat'] = cur['ct'] - cur['at']
    cur['wt']  = cur['tat'] - cur['bt']
    cur['done'] = True
    done += 1


print("\nPID\tAT\tBT\tPR\tCT\tTAT\tWT")
total_tat = total_wt = 0
for p in sorted(proc, key=lambda x: x['idx']):
    print(f"{p['pid']}\t{p['at']}\t{p['bt']}\t{p['pr']}\t{p['ct']}\t{p['tat']}\t{p['wt']}")
    total_tat += p['tat']; total_wt += p['wt']


print(f"\nAverage TAT: {total_tat/n:.2f}")
print(f"Average WT : {total_wt/n:.2f}")


