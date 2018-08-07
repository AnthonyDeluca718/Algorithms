def middle(list_node):
  slow = list_node
  fast = list_node

  while True:
    if fast:
      fast = fast.next
      if fast == slow:
        return Node('Loop')
    else:
      return slow

    if (fast):
      fast = fast.next
      slow = slow.next
      if fast == slow:
        return Node('Loop')
    else:
      return slow



from node import Node

n0 = Node(1)
itr = n0
maximum = 10
for n in range(maximum):
  itr.append_after(Node(n+1))
  itr = itr.next

itr.prev.next = n0

print(middle(n0).val)
