# Heap-Graph-Exercises

Note on Heap sorting Algorithm:

Heap sort is a comparison-based sorting algorithm that uses a binary heap data structure.

Time Complexity - Building the heap: O(n)
Extracting elements and heapifying: O(n log n)
Space Complexity  - O(1)

Steps of Heap Sort
Build a Max Heap from the input data.
Extract the maximum element (the root of the heap) and place it at the end of the array.
Reduce the size of the heap by one and heapify the root of the tree.
Repeat steps 2 and 3 until the size of the heap is reduced to one.
