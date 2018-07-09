class MinStack:
  def __init__(self):
    self.list = []
    self.minima = []

  def push(self, val):
    self.list.append(val)
    if (len(self.minima) == 0 or val <= self.minima[-1]):
      self.minima.append(val)

  def pop(self):
    if (self.list[-1] <= self.minima[-1]):
      self.minima.pop()
    return self.list.pop()

  def min(self):
    return self.minima[-1]


x = MinStack()
x.push(1)
x.push(2)
x.push(3)
x.push(-1)
x.push(0)

print(x.min())
x.pop()
print(x.min())
x.pop()
print(x.min())
x.pop()
print(x.min())
x.pop()
print(x.min())
x.pop()
