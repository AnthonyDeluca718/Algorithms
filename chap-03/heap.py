class Heap: #this is a min heap
  def __init__(self):
    self.arr = []

  def push(self, val):
    self.arr.append(val)
    self.rectify_up(len(self.arr) - 1)

  def pop(self):
    if len(self.arr) == 0:
      return

    self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
    ret = self.arr.pop()
    self.rectify_down(0)
    return ret

  def rectify_down(self, n):
    left = self.left(n)
    right = self.right(n)
    # print('left: ' + str(left))
    if not left:
      return
    child_idx = right if right and self.arr[right] < self.arr[left] else left

    if self.arr[n] > self.arr[child_idx]:
      self.arr[n], self.arr[child_idx] = self.arr[child_idx], self.arr[n]
      self.rectify_down(child_idx)

  def rectify_up(self, n):
    if n < 1:
      return
    pidx = (n-1) // 2
    if self.arr[pidx] > self.arr[n]:
      self.arr[n], self.arr[pidx] = self.arr[pidx], self.arr[n]
      self.rectify_up(pidx)

  def left(self, n):
    idx = 2*n+1
    return idx if idx < len(self.arr) else None

  def right(self, n):
    idx = 2*n+2
    return idx if idx < len(self.arr) else None

  @property
  def length(self):
    return len(self.arr)
