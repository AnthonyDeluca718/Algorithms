import gmpy2

class Hash:
  def __init__(self):
    self.count = 0
    self.pile_count = 7
    self.piles = [[] for x in range(self.pile_count)]

  def find(self, key):
    pile = hash(key) % self.pile_count
    for idx, val in enumerate(self.piles[pile]):
      if key == val[0]:
        return [pile, idx]
    return None

  def set(self, key, val):
    location = self.find(key)
    if location:
      self.piles[location[0]][location[1]][1] = val
    elif self.count < 5 * self.pile_count:
      pile = hash(key) % self.pile_count
      self.piles[pile].append([key, val])
      self.count = self.count + 1
    else:
      self.rebuild()
      self.set(key, val)

  def get(self, key):
    location = self.find(key)
    if location:
      return self.piles[location[0]][location[1]][1]
    else:
      return None

  def rebuild(self):
    print('rebuild')
    self.pile_count = gmpy2.next_prime(2 * self.pile_count)
    current_piles = self.piles
    self.piles = [[] for x in range(self.pile_count)]
    for pile in current_piles:
      for pair in pile:
        self.set(pair[0], pair[1])


hash_map = Hash()

hash_map.set('A', 1)
hash_map.set('B', 2)
hash_map.set('C', 3)
for n in range(100):
  hash_map.set(str(n), n)
hash_map.set('100', 'one hundred')

print(hash_map.get('A'))
print(hash_map.get('99'))
print(hash_map.get('100'))

# n = 2
# while n < 10000:
#   print(n)
#   n = gmpy2.next_prime(2*n)
