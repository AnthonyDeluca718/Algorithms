def uniq(arr):
  elements = {}
  for x in arr:
    if (not x in elements):
      elements[x] = 1
    else:
      elements[x] = elements[x] + 1

  return [ x for x in elements.keys() if elements[x] == 1 ]

arr = [1, 1, 1, 2, 3, 4, 5, 5, 6]
print(uniq(arr))
