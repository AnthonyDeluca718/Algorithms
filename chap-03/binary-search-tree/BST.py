class ListNode:
  def __init__(self, key, val):
    self.key = key
    self.val = val
    self.next = None

  def append(key, val):
    new_node = ListNode(key, val)
    new_node.next = self.next
    self.next = new_node

class BST:
  def __init__(self, key, val, parent=None):
    self.key = key
    self.val = val
    self.left = None
    self.right = None
    self.parent = parent

  def get(self, key):
    if self.key == key:
      return self
    elif self.left and self.key > key:
      return self.left.get(key)
    elif self.right and self.key < key:
      return self.right.get(key)
    else:
      return None

  def set(self, key, val):
    if self.key == key:
      self.val = val
    elif self.key > key:
      if self.left:
        self.left.set(key, val)
      else:
        self.left = BST(key, val, self)
    else:
      if self.right:
        self.right.set(key, val)
      else:
        self.right = BST(key, val, self)

  def equals(self, bst):
    if not (bst.key == self.key and bst.val == self.val):
      return False

    if (self.left):
      if not (bst.left and self.left.equals(bst.left)):
        return False

    if (self.right):
      if not (bst.right and self.right.equals(bst.right)):
        return False

    return True

  @property
  def min(self):
    if self.left:
      return self.left.min
    return self

  @property
  def max(self):
    if self.right:
      return self.right.max
    return self

  @property
  def linked_list(self):
    node = ListNode(self.key, self.val)
    if self.left:
      left_start, left_end = self.left.linked_list
    if self.right:
      right_start, right_end = self.right.linked_list

    start = node
    end = node
    if (self.left):
      start = left_start
      left_end.next = node

    if (self.right):
      end.next = right_start
      end = right_end

    return start, end

  @property
  def sorted_values(self):
    left = self.left.sorted_values if self.left else []
    right = self.right.sorted_values if self.right else []

    return left + [self.val] + right

  def new_child(self, key, node):
    if (self.left and self.left.key == key):
      self.left = node
    elif (self.right and self.right.key == key):
      self.right = node

  def remove_self(self):
    if(self.right):
      next_node = self.right.min
      self.val = next_node.val
      self.key = next_node.key
      next_node.remove_self()
    elif(self.left):
      next_node = self.left.max
      self.val = next_node.val
      self.key = next_node.key
      next_node.remove_self()
    else:
      self.parent.new_child(self.key, None)


  def remove(self, key):
    node = self.get(key)
    if (node):
      node.remove_self()


import random
maxima = 100
for count in range(10):
  sorted_arr = list(range(maxima))
  arr = list(range(0, maxima))
  random.shuffle(arr)
  b = BST(arr[0], arr[0], None)
  for i in range(1, len(arr)):
    x = arr[i]
    b.set(x, x)

  del sorted_arr[sorted_arr.index(4)]
  del sorted_arr[sorted_arr.index(2)]
  del sorted_arr[sorted_arr.index(27)]
  del sorted_arr[sorted_arr.index(68)]
  del sorted_arr[sorted_arr.index(86)]
  b.remove(4)
  b.remove(2)
  b.remove(27)
  b.remove(68)
  b.remove(86)

  if sorted_arr == b.sorted_values:
    print(True)
  else:
    print(sorted_arr)
    print(b.sorted_values)
