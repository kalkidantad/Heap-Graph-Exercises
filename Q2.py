
"""function that starts from the last non-leaf node (heap_size // 2) and moves backward to the root and calls max_heapify for each node """

def heapify(A):
   
    for i in range(A['heap_size'] // 2, 0, -1):
        max_heapify(A, i)

def left(i):
    return 2 * i

def right(i):
    return 2 * i + 1

def max_heapify(A, i):
    largest = i
    heap_size = A['heap_size']

    while True:
        l = left(i)
        r = right(i)

        if l <= heap_size and A['array'][l] > A['array'][largest]:
            largest = l

        if r <= heap_size and A['array'][r] > A['array'][largest]:
            largest = r

        if largest == i:
            break

        A['array'][i], A['array'][largest] = A['array'][largest], A['array'][i]
        i = largest

A = {
    'array': [0,30,10,20,40,5,15],  
    'heap_size': 6  
}

heapify(A)
print(A['array'])  
