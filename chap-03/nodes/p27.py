def loop_count(list_node):
  slow = list_node
  fast = list_node

  count = 0
  while True:
    if fast:
      fast = fast.next
    else:
      return None

    if fast:
      fast = fast.next
      slow = slow.next
      count += 1
      if fast == slow:
        return count
    else:
      return None

def loop_finder(list_node):
  count = loop_count(list_node)
  if not count:
    return Node('No Loop')

  follow = list_node
  lead = list_node
  for i in range(count):
    lead = lead.next

  while(follow != lead):
    follow = follow.next
    lead = lead.next

  return follow


from node import Node

n0 = Node(0)
itr = n0
maximum = 16
nodes = {0: n0}
for n in range(maximum):
  new_node = Node(n+1)
  nodes[n+1] = new_node
  itr.append_after(new_node)
  itr = itr.next

nodes[10].next = nodes[9]
print( loop_finder(n0).val )
