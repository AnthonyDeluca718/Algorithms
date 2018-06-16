def fast_int_exp(a, n):
  if (n <= 0):
    return 1
  elif (n % 2 == 0):
    return fast_int_exp(a, n // 2) ** 2
  else:
    return fast_int_exp(a, n // 2) ** 2 * a

print (fast_int_exp(2.3, 5))
print (2.3 ** 5)
print (fast_int_exp(2.3, 8))
print (2.3 ** 8)
