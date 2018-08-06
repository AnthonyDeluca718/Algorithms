def binary_search(arr, target, **indices):
  i = 0
  j = len(arr)
  if ('i' in indices):
    i = indices['i']
  if ('j' in indices):
    j = indices['j']

  # print(str(i) + ' ' + str(j))

  if (j - i == 1):
    return i if arr[i] == target else -1
  elif (j == i):
    return -1

  mid = (i + j) // 2
  if (arr[mid] == target):
    return mid
  elif (arr[mid] > target):
    return binary_search(arr, target, i=i, j=mid)
  else:
    return binary_search(arr, target, i=mid+1, j=j)


arr = list(range(0, 100))
print( binary_search(arr, 97) )
print( binary_search([12, 14], 14))
