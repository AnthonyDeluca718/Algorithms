def common_pair(string):
  arr = string.split(' ')
  counts = {}
  for i in range(1, len(arr)):
    pair = arr[i-1] + ' ' + arr[i]
    if (pair in counts):
      counts[pair] = counts[pair] + 1
    else:
      counts[pair] = 1

  maximum = max(counts, key=counts.get)
  max_count = counts[maximum]
  maxes = [key for key in counts.keys() if counts[key] == max_count]
  return maxes

print(common_pair('imma get yolo cash money imma get some cash money baby'))
