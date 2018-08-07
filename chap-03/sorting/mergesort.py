def merge(arr1, arr2):
  res = []
  i = 0
  j = 0
  while(i < len(arr1) and j < len(arr2)):
    if (arr1[i] > arr2[j]):
      res.append(arr2[j])
      j += 1
    else:
      res.append(arr1[i])
      i += 1

  res.extend(arr1[i:])
  res.extend(arr2[j:])

  return res

# a1 = [0, 2, 4, 6, 8]
# a2 = [1, 3, 5, 7, 9]
# print(merge(a1, a2))

def mergesort(arr):
  if (len(arr) < 2):
    return arr

  mid = len(arr) // 2
  arr1 = mergesort(arr[:mid])
  arr2 = mergesort(arr[mid:])

  return merge(arr1, arr2)

# import random
# sorted_arr = list(range(100))
# arr = list(range(100))
#
# for x in range(10):
#   random.shuffle(arr)
#   merge_sorted = mergesort(arr)
#   print(merge_sorted == sorted_arr)
