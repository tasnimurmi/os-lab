def fifoPR(pages, cap):
    frames = [-1] * cap
    order = []
    page_frame = {}
    faults = 0

    for p in pages:
        if p not in page_frame:
            faults += 1
            placed = False

            for f in range(cap):
                if frames[f] == -1:
                    frames[f] = p
                    page_frame[p] = f
                    order.append(f)
                    placed = True
                    break

            if not placed:
                victim = order.pop(0)
                old_page = frames[victim]
                del page_frame[old_page]
                frames[victim] = p
                page_SSframe[p] = victim
                order.append(victim)

        print(" ".join(str(f) if f != -1 else "-" for f in frames))

    print("Total Page Faults:", faults)


# Example usage
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3]
frames = 3
fifoPR(pages, frames)
