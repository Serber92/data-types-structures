class Node:

  def __init__(self, char):
    self.char = char
    self.children = {}
    self.word_finished = False
    self.counter = 0

class Trie:

  def __init__(self):
    self.root = Node('*') # to make the root empty

  def insert(self, word):
    current = self.root

    for char in word:

      if char in current.children:
        current = current.children[char]
        current.counter += 1
      else:
        new_node = Node(char)
        current.children[char] = new_node
        current = new_node
        current.counter += 1

    current.word_finished = True

  def search(self, word):
    if not self.root.children:
      return False
    
    current = self.root

    for char in word:

      if char in current.children:
        current = current.children[char]
      else:
        return False
    
    if current.word_finished:
      return True
      
    return False
