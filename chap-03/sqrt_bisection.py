def sqrt(y):
  tol = 10 ** -12

  lower = 0
  upper = max(y, 1)
  x = y/2

  while(abs(x **2 - y) > tol):
    if (x ** 2 < y):
      lower = (lower + upper)/2
    else:
      upper =  (lower + upper)/2

    x = (upper + lower)/2

  return x

print (sqrt(9))
print (sqrt(5))
print (sqrt(0.5))
print (sqrt(1))
