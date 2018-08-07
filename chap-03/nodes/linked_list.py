from node import Node

class LinkedList:
  def __init__(self):
    self.list = None
    self.first = None
    self.last = None
    self.length = 0

  def append_after(self, el, val):
    new_node = Node(val)
    new_node.prev = el
    new_node.next = el.next
    if (not el.next):
      self.last = new_node
    el.next = new_node
    self.length += 1

  def append_before(self, el, val):
    new_node = Node(val)
    new_node.next = el
    new_node.prev = el.prev
    if (not el.prev):
      self.first = new_node
    el.prev = new_node
    self.length += 1

  def remove(self, el):
    if el.prev and el.next:
      el.prev.next = el.next
      el.next.prev = el.prev
      self.length -= 1
    elif el.prev: #end of list
      el.prev.next = None
      self.length -= 1
    elif el.next: #begin of list
      el.next.prev = None
      self.length -= 1

  def push(self, val):
    if self.length == 0:
      new_node = Node(val)
      self.first = new_node
      self.last = new_node
      self.length = 1
    else:
      self.append_after(self.last, val)

  def unshift(self, val):
    if (self.length == 0):
      self.push(val)
    else:
      self.append_before(self.first, val)

  def pop(self):
    if (self.length > 0):
      self.remove(self.last)

  def shift(self):
    if (self.length > 0):
      self.remove(self.first)

  def find(self, val):
    el = self.first
    while(el):
      if el.val == val:
        return el
      el = el.next
    return None


llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.unshift(0)
llist.unshift(-1)
llist.push(5)

element = llist.find(3)
llist.append_after(element, 3.01)
llist.append_before(element, 2.99)
llist.remove(element)

el = llist.first
while(el):
  print(el.val)
  el = el.next

print('length: ' + str(llist.length))
