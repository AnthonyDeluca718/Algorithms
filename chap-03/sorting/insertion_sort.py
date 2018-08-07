def insertion_sort(arr, **indices):
  i = 0
  j = len(arr)
  if ('i' in indices):
    i = indices['i']
  if ('j' in indices):
    j = indices['j']
  length = j - 1

  if length < 2:
    return arr

  start = j - 2

  while (start >= i):
    idx = start
    while (idx < j -1 and arr[idx] > arr[idx+1]):
      temp = arr[idx+1]
      arr[idx+1] = arr[idx]
      arr[idx] = temp
      idx += 1
    start -= 1


import random
sorted_arr = list(range(100))
arr = list(range(100))

# for x in range(10):
#   random.shuffle(arr)
#   insertion_sort(arr)
#   print(arr == sorted_arr)

# random.shuffle(arr)
# insertion_sort(arr, i=0, j=50)
# print(arr)
