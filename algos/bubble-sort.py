############################

def bubbleSort(alist):
    loops = len(alist) - 1

    while loops > 0:
        for i in range(loops):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
        loops -= 1
    
    return alist

alist = [54,26,93,17,77,31,44,55,20]

print bubbleSort(alist)
