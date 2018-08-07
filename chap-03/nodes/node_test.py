from node import Node

n0 = Node(0)
itr = n0
for n in range(1, 11):
  itr.append_after(Node(n))
  itr = itr.next

el = n0
while el:
  print(el.val)
  el = el.next
