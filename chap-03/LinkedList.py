class Link:
  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None

class LinkedList:
  def __init__(self):
    self.begin = Link(None)
    self.end = Link(None)
    self.begin.next = self.end
    self.end.prev = self.begin
    self.first = None
    self.last = None

  def append(self):


  def remove(self):

  def insert_after(self, node):
