"""it extracts the elements from the heap in a looop and swap the max element with the last element in the heap """

def heap_sort(A):
  
    build_max_heap(A)
    
    for i in range(A['heap_size'], 1, -1):

        A['array'][1], A['array'][i] = A['array'][i], A['array'][1]
        A['heap_size'] -= 1

        max_heapify(A, 1)

def build_max_heap(A):
    A['heap_size'] = len(A['array']) - 1  

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
    'array': [0, 10, 20, 30, 5, 15, 25],  
    'heap_size': 6  
}

heap_sort(A)
print(A['array'][1:])  
