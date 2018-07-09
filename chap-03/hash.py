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
    self.pile_count = gmpy2.next_prime(2 * self.pile_count)
    current_piles = self.piles
    self.piles = [[] for x in range(self.pile_count)]
    for pile in current_piles:
      for pair in pile:
        self.set(pair[0], pair[1])

  def remove(self, key):
    location = self.find(key)
    if location:
      self.count = self.count - 1
      pile = self.piles[location[0]]
      el = pile[location[1]][1]
      del pile[location[1]]
      # pile.remove[el]
      return el
    else:
      return None
