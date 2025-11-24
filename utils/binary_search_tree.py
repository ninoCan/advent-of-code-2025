from utils.tree_node import TreeNode 

class BST:
  def __init__(self):
    self.root = None

    def insert_at_beginning(self,data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
            return
        self.tail = new_node      
        self.head = new_node

    def insert(self, data):
        new_node = TreeNode(data)
        # Check if the BST is empty
        if self.root is None:
            self.root = new_node
            return
        else:
            current_node = self.root
            while True:
                if data < current_node:
                    if current_node.left_child is None:
                        current_node.left_child = new_node
                        return 
                    else:
                        current_node = current_node.left_child
                elif data > current_node:
                    if current_node.right_child is None:
                        current_node.right_child = new_node
                        return
                    else:
                        current_node = current_node.right_child
                else:
                    self.insert_at_beginning(current_node.data)

    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            else:
                current_node = current_node.next
        return False

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
