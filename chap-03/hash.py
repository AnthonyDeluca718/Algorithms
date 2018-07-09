import gmpy2

class Hash:
  def __init__(self):
    self.count = 0
    self.pile_count = 1
    self.piles = [] * self.pile_count

hash_map = Hash()
# print(hash_map.piles)

n = 2
while n < 10000:
  print(n)
  n = gmpy2.next_prime(2*n)
