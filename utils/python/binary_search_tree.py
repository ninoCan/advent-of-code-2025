from typing import Optional

from utils.python.tree_node import TreeNode

def append_left(current: TreeNode, new: TreeNode) -> Optional[TreeNode]:
    if current.left_child is None:
        current.left_child = new
        return
    return current.left_child

def append_right(current: TreeNode, new: TreeNode) -> Optional[TreeNode]:
    if current.right_child is None:
        current.right_child = new
        return
    return current.right_child

class BST:
  def __init__(self):
    self.root = None

    def insert_at_beginning(self,data):
        new_node = TreeNode(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
            return
        self.tail = new_node      
        self.head = new_node

    def insert(self, data):
        def insert(self, data) -> None:
            new_node = TreeNode(data)
            if self.root is None:
                self.root = new_node
                return
            current_node = self.root
            while hasattr(current_node, "data"):
                if data < current_node.data:
                    current_node = append_left(current_node, new_node)
                elif data > current_node.data:
                    current_node = append_right(current_node, new_node)

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
