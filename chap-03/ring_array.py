# shift
# unshift
# push
# pop
# set
# get
# length

class CArray:
  def __init__(self, length):
    self.list = [None] * length

  def set(self, idx, val):
    self.list[idx] = val

  def get(self, idx):
    return self.list[idx]

class RingArray:
  def __init__(self):
    self.max_len = 2
    self.arr = CArray(self.max_len)
    self.length = 0
    self.start = 0

  def index(self, idx):
    return (self.start + idx) % self.max_len

  def get(self, idx):
    return self.arr.get(self.index(idx))

  def rebuild(self):
    self.max_len = 2*self.max_len
    new_list = CArray(self.max_len)
    for j in range(self.length):
      new_list.set(j, self.get(j))
    self.start = 0
    self.arr = new_list

  def push(self, val):
    if (self.length < self.max_len):
      self.arr.set(self.index(self.length), val)
      self.length = self.length + 1
    else:
      self.rebuild()
      self.push(val)

my_array = RingArray()
my_array.push(1)
my_array.push(2)
my_array.push(3)
my_array.push(4)
my_array.push(5)
my_array.push(6)

print(my_array.get(0))
print(my_array.get(1))
print(my_array.get(2))
print(my_array.get(3))
print(my_array.get(4))
print(my_array.get(5))
