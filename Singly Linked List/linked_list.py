class Node:
  # An object for storing a single node of a linked list.
  # Models 2 attributes - data and the link to the next node in the list
  data = None
  next_node = None

  def __init__(self, data):
    self.data = data

  def __repr__(self):
    return "<Node data: %s>" % self.data  
 
class LinkedList:
# Singly linked list

  def __init__(self):
    self.head = None

  def __repr__(self):
    nodes = []
    current = self.head
    while current:
      nodes.append(str(current.data))
      current = current.next_node
    return " -> ".join(nodes)   

  def is_empty(self):
    return self.head == None
  
  def size(self):
    current =  self.head
    count = 0

    while current:
      count += 1
      current = current.next_node

    return count

  def add(self, data):
  # Adds new Node containing data at head of the List
    new_node = Node(data)
    new_node.next_node = self.head
    self.head = new_node

  def search(self, key):
    current = self.head

    while current:
      if current.data == key:
        return current
      else:
        current = current.next_node
    return None
  
  def insert(self, data, index):
    if index < 0 or index > self.size():
      raise IndexError("Index out of bounds")
      
    if index == 0:
      self.add(data)
      return
    
    current = self.head
    count  = 0

    while current:
      if count == index - 1:
        new_node = Node(data)
        new_node.next_node = current.next_node
        current.next_node = new_node
        return
      current = current.next_node
      count += 1

    return
  
  def remove(self, key):
    current = self.head
    previous = None
    found  = False
    
    while current and not found:
      if current.data == key and current is self.head:
        found = True
        self.head = current.next_node
      elif current.data == key:
        found =  True
        previous.next_node = current.next_node
      else:
        previous = current
        current = current.next_node

    return current
  
  def node_at_index(self, index):
    if index == 0:
      return self.head
    else:
      current = self.head
      position = 0

      while position < index:
        current = current.next_node
        position += 1
      
      return current

if __name__ == "__main__":
  l = LinkedList()
  l.add(1)
  l.add(2)
  l.add(3)
  l.add(4)
  l.add(5)

  print(l.size()) # 5
  print(l.is_empty()) # False
  print(l.head) # <Node data: 5>
  print(l.insert(8, 2))
  print(l.__repr__()) # 5 -> 4 -> 3 -> 2 -> 1
  print(l.search(3)) # <Node data: 3>