import copy

from typing import Any, Optional

class TreeNode:
    def __init__(
        self,
        data: Any,
        left: Optional[TreeNode] = None,
        right: Optional[TreeNode] = None,
    ) -> None:
       self.data = data 
       self.left_child = left
       self.right_child = right
    
    def copy(self) -> TreeNode:
        return copy.deepcopy(self)
