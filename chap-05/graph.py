# TODO: handle unlabeled graphs later

# Graph is a dict of dicts:
# nodes = dict where the keys are labels and the values are nodes
# edges = dict where the keys are labels and the value is an adjacency list
# adjacency list: dict where the keys are
#
#
#

# The MultiGraph class uses a dict-of-dict-of-dict-of-dict data structure. The outer dict (node_dict) holds adjacency information keyed by node. The next dict (adjlist_dict) represents the adjacency information and holds edge_key dicts keyed by neighbor. The edge_key dict holds each edge_attr dict keyed by edge key. The inner dict (edge_attr_dict) represents the edge data and holds edge attribute values keyed by attribute names.

class Graph:
  def __init__(self, directed=False):
    self.vertices = {}
    self.directed = directed

  def bread_first(self, node, func):
    func(node)
    children = {}


  @property
  def num_vertices(self):
    return len(self.vertices)
