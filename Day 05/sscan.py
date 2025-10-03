def scan(req, head, dir):
    seek_count = 0


    left = [r for r in req if r < head]
    right = [r for r in req if r >= head]


    left.sort()
    right.sort()


    if dir == "left":
   
        if left:
           
            seek_count += abs(head - left[0])
            head = left[0]


         
            if right:
                seek_count += abs(head - right[-1])
        else:
         
            if right:
                seek_count += abs(head - right[-1])


    elif dir == "right":
     
        if right:
         
            seek_count += abs(head - right[-1])
            head = right[-1]


         
            if left:
                seek_count += abs(head - left[0])
        else:
           
            if left:
                seek_count += abs(head - left[0])




    return seek_count




if __name__ == "__main__":
    req = list(map(int, input("Enter the req: ").split()))
    head = int(input("Enter the cur head pos: "))
    dir = input("Enter head dir: ").lower()


    if dir not in ['left', 'right']:
        print("Invalid direction!.")
    else:
        total_seek = scan(req, head, dir)
        print(f"Total seek time (head movement): {total_seek}")

