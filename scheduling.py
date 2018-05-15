def optimal(arr):
  intervals = sorted(arr, key = lambda a: a[1])
  i = 0
  output = []
  while (i < len(intervals)):
    output.append(intervals[i])
    end_time = intervals[i][1]
    i += 1
    while (i < len(intervals) and intervals[i][0] < end_time):
      i += 1
  return output


arr = [[1, 2], [1.5, 3], [0, 1], [5, 5.6], [1.6, 1.8]]
print( optimal(arr) )
