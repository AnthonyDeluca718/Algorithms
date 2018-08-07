# 3-23 - Implement an algorithm to reverse a linked list. Now do it without recursion.

def recursive_reverse(list_node): #this works for singly linked if append_after is implemented corrected
  if not list_node.next:
    return list_node

  end = recursive_reverse(list_node.next)
  end.append_after(list_node)
  return list_node

def reverse_list(list_node):
  itr = list_node
  while itr.next:
    itr = itr.next
  end = itr

  while(itr):
    next_node = itr.prev
    itr.prev = itr.next
    itr.next = next_node
    itr = next_node

  return end

def reverse_singly_linked(list_node): #this works for singly linked if append_after is implemented corrected
  elements = {}
  i = 0
  itr = list_node

  while itr:
    elements[i] = itr
    i += 1
    itr = itr.next

  maximum = i-1

  for n in range(maximum, 0, -1):
    el = elements[n]
    el.append_after(elements[n-1])

  return nodes[maximum]





from node import Node

n0 = Node(0)
itr = n0
maximum = 10
nodes = {}
for n in range(maximum):
  new_node = Node(n+1)
  nodes[n+1] = new_node
  itr.append_after(new_node)
  itr = itr.next

reverse_singly_linked(n0)

el = nodes[maximum]
while el:
  print(el.val)
  el = el.next

# itr.prev.next = n0
