from insertion_sort import insertion_sort

def swap(arr, i, j):
  temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp

def quicksort(arr, **indices):
  i = 0
  j = len(arr)
  if ('i' in indices):
    i = indices['i']
  if ('j' in indices):
    j = indices['j']

  length = j - i

  if length < 6:
    return insertion_sort(arr, i=i, j=j)

  mid = (i + j) // 2
  if (arr[i] > arr[i] and arr[j] > arr[mid]):
    pidx = i
  elif (arr[j] > arr[i] and arr[i] > arr[mid]):
    pidx = j
  else:
    pidx = mid
  # pidx = 0 # easier to test with initial element as pivot

  pivot = arr[pidx]
  idx = i
  end = j-1
  num_pivots = 0
  while(idx <= end):
    if arr[idx] < pivot:
      idx += 1
    elif arr[idx] == pivot:
      swap(arr, idx, end)
      num_pivots += 1
      end -= 1
    else:
      swap(arr, idx, end)
      swap(arr, end, end + num_pivots)
      end -= 1

  quicksort(arr, i=i, j=idx)
  quicksort(arr, i=end+num_pivots, j=j)





# test = [3, 6, 5, 4, 0, 2, 1]
# quicksort(test)
# print(test)

# import random
# sorted_arr = list(range(100))
# arr = list(range(100))
#
# for x in range(10):
#   random.shuffle(arr)
#   insertion_sort(arr)
#   print(arr == sorted_arr)
