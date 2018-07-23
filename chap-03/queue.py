class Queue:
  def __init__(self):
    self.in_arr = []
    self.out_arr = []

  def length(self):
    return len(self.in_arr) + len(self.out_arr)

  def enqueue(self, el):
    self.in_arr.append(el)

  def dequeue(self):
    if (len(self.in_arr) + len(self.out_arr) == 0):
      return None
    elif (len(self.out_arr) > 0):
      return self.out_arr.pop()
    else:
      self.in_arr.reverse()
      self.out_arr = self.in_arr
      self.in_arr = []
      return self.out_arr.pop()

# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# print(q.dequeue())
# print(f"Length should be 2. Length: {q.length()}.")
# q.enqueue(4)
# q.enqueue(5)
# q.enqueue(6)
# print(f"Length should be 5. Length: {q.length()}.")
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())
# print(f"Length should be 2. Length: {q.length()}.")
# print(q.dequeue())
# print(q.dequeue())
# print(f"Length should be 0. Length: {q.length()}.")
