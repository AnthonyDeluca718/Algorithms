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

  def new_child(self, key, node):
    if (self.left and self.left.key == key):
      print('parent: ' + str(self.key))
      print('left: ' + str(node.key))
      self.left = node
      node.parent = self
    elif (self.right and self.right.key == key):
      print('parent: ' + str(self.key))
      print('right: ' + str(node.key))
      self.right = node
      node.parent = self

  def remove_self(self):
    if self.right:
      self.val = self.right.val
      self.key = self.right.key
      self.right.remove_self()
      if (self.right):
        print(self.right.key > self.key)
    elif self.left and self.parent:
      print('parent left')
      self.parent.new_child(self.key, self.left)
      # self.val = self.left.val
      # self.key = self.left.key
      # self.left.remove_self()
      # if self.left and self.left.key > self.key:
      #   self.val, self.left.val = self.left.val, self.val
      #   self.key, self.left.key = self.left.key, self.key
    elif self.left:
      print('no-parent-left: ' + str(selef.left.key))
      node = self.left
      self.key = node.key
      self.val = node.val
      self.left = node.left
      self.right = node.right
      self.left.parent = self
      self.righ.parent = self

      if node.left:
        node.left.parent = self
      if node.right:
        node.right.parent = self
    elif self.parent:
      if self.parent.left and self.parent.left.key == self.key:
        self.parent.left = None
      elif self.parent.right and self.parent.right.key == self.key:
        self.parent.right = None

  def remove(self, key):
    node = self.get(key)
    if (node):
      node.remove_self()


import random
maxima = 30
# for count in range(5):
sorted_arr = list(range(maxima))
# arr = list(range(0, maxima))
arr = [29, 19, 21, 26, 25, 2, 17, 6, 9, 24, 8, 16, 11, 14, 22, 23, 28, 13, 15, 18, 0, 27, 10, 7, 1, 12, 20, 4, 5, 3]
# random.shuffle(arr)
b = BST(arr[0], arr[0], None)
for i in range(1, len(arr)):
  x = arr[i]
  b.set(x, x)

del sorted_arr[4]
del sorted_arr[2]
# del sorted_arr[27]
# del sorted_arr[68]
# del sorted_arr[86]
b.remove(4)
b.remove(2)
# b.remove(27)
# b.remove(68)
# b.remove(86)
print(True if sorted_arr == b.sorted_values else b.sorted_values)

  # def left_right(self, key):
  #   if self.left and self.left.key == key:
  #     return 'left'
  #   elif self.right and self.right.key == key:
  #     return 'right'
  #   else:
  #     return None
  #



# for count in range(5):
#   sorted_arr = list(range(100))
#   arr = list(range(0, 100))
#   random.shuffle(arr)
#   b = BST(arr[0], arr[0], None)
#   for i in range(1, len(arr)):
#     x = arr[i]
#     b.set(x, x)
#
#   new_arr=[]
#   itr, _ = b.linked_list
#   while itr:
#     new_arr.append(itr.val)
#     itr = itr.next
#
#   print(new_arr == sorted_arr)

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
