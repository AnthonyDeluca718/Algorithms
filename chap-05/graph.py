# TODO: handle unlabeled graphs later

# Graph is a dict of dicts:
# nodes = dict where the keys are labels and the values are nodes
# edges = dict where the keys are labels and the value is an adjacency list
# adjacency list: dict where the keys are
#
#
#

# The MultiGraph class uses a dict-of-dict-of-dict-of-dict data structure. The outer dict (node_dict) holds adjacency information keyed by node. The next dict (adjlist_dict) represents the adjacency information and holds edge_key dicts keyed by neighbor. The edge_key dict holds each edge_attr dict keyed by edge key. The inner dict (edge_attr_dict) represents the edge data and holds edge attribute values keyed by attribute names.

# https://bradfieldcs.com/algos/graphs/representing-a-graph/

# vertices:
# label
# neighbors - list of ids of the neighbors
# graph - pointer to the graph
# optionally: can have other properties such as a geometric position in space

from collections import deque

class Edge:
  def __init__(self, weight, data):
    self.weight = weight
    for key in data:
      setattr(self, key, data[key])

class Vertex:
  def __init__(self, label, val, **data):
    self.label = label
    self.val = val
    self.graph = None
    self.adjacency = {}
    for key in data:
      setattr(self, key, data[key])

  def breadth_first(self, func, enqueued={}, nodes=deque()):
    func(self)
    enqueued[self.label] = True
    for node in self.neighbors:
      if not node.label in enqueued:
        enqueued[node.label] = True
        nodes.append(node)

    if len(nodes) > 0:
      el = nodes.popleft()
      el.breadth_first(func, enqueued, nodes)

  def depth_first(self, func, handled={}):
    func(self)
    handled[self.label] = True
    for node in self.neighbors:
      if not node.label in handled:
        node.depth_first(func, handled)


  @property
  def neighbors(self):
    return [self.graph.vertices[key] for key in self.adjacency]


class Graph:
  def __init__(self, directed=False):
    self.vertices = {}
    self.directed = directed

  def add_vertex(self, vertex):
    vertex.graph = self
    self.vertices[vertex.label] = vertex

  def add_edge(self, n1, n2, weight=1, **data):
    edge = Edge(weight, data)
    self.vertices[n1].adjacency[n2] = edge

    if not self.directed:
      self.vertices[n2].adjacency[n1] = edge

  @property
  def num_vertices(self):
    return len(self.vertices)

g = Graph()
for i in range(10):
  v = Vertex(i, i)
  g.add_vertex(v)

for i in range(10):
  g.add_edge(i, (i + 1) % 10)

# for i in range(10):
#   v = g.vertices[i]
#   print(v.val)

v = g.vertices[0]
def print_val(node):
  print(node.val)

v.breadth_first(print_val)
# v.depth_first(print_val)
