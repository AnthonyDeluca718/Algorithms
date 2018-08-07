class Node:
  def __init__(self, val):
    self.val = val
    self.prev = None
    self.next = None

  def append_after(self, node):
    if (self.next):
      self.next.prev = node
    node.prev = self
    node.next = self.next
    self.next = node

  def append_before(self, node):
    if (self.prev):
      self.prev.next = node
    node.next = self
    node.prev = self.prev
    self.prev = node
