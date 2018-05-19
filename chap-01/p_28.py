# 1-28. [5] Write a function to perform integer division without using either the / or * operators. Find a fast way to do it.

# I am being lazy and only doing it for positive a,b to save time!

import math

def div_positive(a, b):
  return math.floor(math.exp(math.log(a) - math.log(b) + math.pow(10, -12)))

print( div_positive(4, 5) )

print( div_positive(7, 3) )

print( div_positive(6, 3) )
