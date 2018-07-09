def product(arr):
  n = len(arr)

  if n == 0:
    return []
  elif n == 1:
    return [1]

  left = [arr[0]]
  right = [arr[-1]]

  for i in range(1, n):
    left.append(left[-1]*arr[i])
    right.append(right[-1]*arr[-(i+1)])

  res = [0]*n
  res[0] = right[-2]
  for i in range(1, n):
    res[i] = left[i-1]*right[n-2-i]
  res[n-1] = left[-2]
  return res


arr = [1, 2, 3, 4, 5, 6]
print(product(arr))
