class ListNode:
  def __init__(self, key, val):
    self.key = key
    self.val = val
    self.next = None

  def append(key, val):
    new_node = ListNode(key, val)
    new_node.next = self.next
    self.next = new_node

class BST: #get, set, remove
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

  def left_right(self, key):
    if self.left and self.left.key == key:
      return 'left'
    elif self.right and self.right.key == key:
      return 'right'
    else:
      return None

  def new_child(self, key, node):
    if (self.left and self.left.key == key):
      self.left = node
    elif (self.right and self.right.key == key):
      self.right = node

  def remove_self(self):
    print('remove self')
    if self.right:
      promoted = self.right
      promoted.left = self.left
    elif self.left:
      promoted = self.left
      promoted.right = self.right
    else:
      self = None
      return

    if self.parent:
      self.parent.new_child(promoted)

import random
for count in range(5):
  sorted_arr = list(range(100))
  arr = list(range(0, 100))
  random.shuffle(arr)
  b = BST(arr[0], arr[0], None)
  for i in range(1, len(arr)):
    x = arr[i]
    b.set(x, x)

  new_arr=[]
  itr, _ = b.linked_list
  while itr:
    new_arr.append(itr.val)
    itr = itr.next

  print(new_arr == sorted_arr)




# for count in range(5):
#   arr = list(range(1, 100))
#   random.shuffle(arr)
#   b1 = BST(arr[0], arr[0], None)
#   b2 = BST(arr[0], arr[0], None)
#   for x in range(1, len(arr)):
#     b1.set(x, x)
#     b2.set(x, x)
#   print (b1.equals(b2))
#   b1.set(10, 11)
#   print(b1.equals(b2))


# for count in range(10):
#   maxima = 100
#   sorted_arr = list(range(maxima))
#   arr = list(range(maxima))
#   random.shuffle(arr)
#   bst = BST(arr[0], arr[0], None)
#   for i in range(1, len(arr)):
#     x = arr[i]
#     bst.set(x, x)
#
#   print(bst.sorted_values == sorted_arr)
