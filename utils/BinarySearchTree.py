from utils.TreeNode import TreeNode
from typing import Optional

def append_left(current: TreeNode, new: TreeNode) -> Optional[TreeNode]:
    if current.left_child is None:
        current.left_child = new
        return
    return current.left_child

def append_right(current: TreeNode, new: TreeNode)
    if current.right_child is None:
        current.right_child = new
        return
    return current.right_child

class BST:
    def __init__(
        self,
        root: Optional[TreeNode] = None
    ):
        self.root = root


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


