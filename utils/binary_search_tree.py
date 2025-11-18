class BST:
  def __init__(self):
    self.root = None

  def insert(self, data):
    new_node = TreeNode(data)
    # Check if the BST is empty
    if self.root ==None:
      self.root = new_node
      return
    else:
      current_node = self.root
      while True:
        # Check if the data to insert is smaller than the current node's data
        if data < current_node:
          if current_node.left_child == None:
            current_node.left_child = new_node
            return 
          else:
            current_node = current_node.left_child
        # Check if the data to insert is greater than the current node's data
        elif data > current_node:
          if current_node.right_child == None:
            current_node.right_child = new_node
            return
          else:
            current_node = current_node.right_child


    def find_min(self):
        current_node = self.root
        while current_node.left_child:
            current_node = current_node.left_child
        return current_node.data

    def find_max(self):
        current_node = self.root
        while current_node.right_child:
            current_node = current_node.right_child
        return current_node.data

    def deep_first_visit(self, current_node):
        if current_node:
            self.in_order(current_node.left_child)
            print(current_node.data)
            self.in_order(current_node.right_child)
