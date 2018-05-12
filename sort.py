def insertion_sort (arr):
  length = len(arr)

  for j in reversed(range(1, length)):
    i = j-1
    while(i < length-1 and arr[i] > arr[i+1]):
      # print(f"{arr[i]}: {arr[j]}")
      arr[i], arr[i+1] = arr[i+1], arr[i]
      # print(f"{arr[i]}: {arr[j]}")
      i = i+1

arr = [5, 6, 4, 3, 2, 1]
insertion_sort(arr)
print(arr)
