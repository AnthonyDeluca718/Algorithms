def zeroes(arr):
  count = 0
  start = 0
  for row in arr:
    i = start
    while (i < len(row)):
      if (row[i] == 0):
        count += 1
        start = i+1
        break
      elif (row[i] > 0):
        start = i
        break
      i += 1

  return count

arr = [
  [-3, 0, 1, 2],
  [-4, -2, 0, 1],
  [-6, -5, -4, 0]
]

print( zeroes(arr) )
