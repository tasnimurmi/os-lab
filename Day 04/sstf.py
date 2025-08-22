def sstf_disk(requests, head):
    total_seek = 0
    current = head
    sequence = []
    print("Seek sequence:", end=" ")
    while requests:
        min_distance = float("inf")
        min_index = -1
        for i, req in enumerate(requests):
            distance = abs(current - req)
            if distance < min_distance:
                min_distance = distance
                min_index = i
        next_req = requests.pop(min_index)
        distance = abs(current - next_req)
        total_seek += distance
        current = next_req
        sequence.append(next_req)
        print(next_req, end=" ")
    print("\nTotal number of seek operations =", total_seek)
    print("Average seek time =", total_seek / len(sequence))

n = int(input("Enter number of requests: "))
requests = []
print("Enter requests:")
for i in range(n):
    req = int(input(f"Request {i+1}: "))
    requests.append(req)
head = int(input("Enter the head position: "))
sstf_disk(requests, head)
