def left(i):
    return 2 * i

def right(i):
    return 2 * i + 1

""" the function uses a dict to track the valid size of the heap and given array with a 1 based index. The function compares the value at index i with its children, and if either child is greater,
    it swaps the values and recursively heapifies the affected subtree """

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

max_heapify(A, 1)  
print(A['array'])  