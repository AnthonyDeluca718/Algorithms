import random
from heap import Heap

def heapsort(arr):
  new_heap = Heap()

  for x in arr:
    new_heap.push(x)

  sorted_arr = []
  while new_heap.length > 0:
    sorted_arr.append(new_heap.pop())

  return sorted_arr

# test
maxima = 100
sorted_arr = list(range(maxima))
arr = list(range(maxima))

for x in range(10):
  random.shuffle(arr)
  heap_sorted = heapsort(arr)
  print(heap_sorted == sorted_arr)
