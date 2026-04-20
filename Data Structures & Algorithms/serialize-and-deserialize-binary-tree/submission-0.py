# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    def __init__(self):
        self.serialized_str = ""
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        return self.do_serialize(root, 0)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.serialized_str =  data + "|"
        return self.do_de_serialize()
        

    def do_serialize(self, node: Optional[TreeNode], index: int) -> str:
         if not node:
            return f"#"
             
         leftVal = self.do_serialize(node.left, 2 * index + 1)
         rightVal = self.do_serialize(node.right, 2 * index + 2)

         return f"{node.val}|{leftVal}|{rightVal}"   


    def do_de_serialize(self) -> Optional[TreeNode]:
        # print(f"ser str {self.serialized_str}")
        boundary = self.serialized_str.find("|")
        candidate = self.serialized_str[0:boundary]
        node = TreeNode()
        self.serialized_str = self.serialized_str[boundary+1:]
        if candidate == "#":
            return None
        # print(f"candidate: {candidate}")    
        node.val = int(candidate)
        node.left = self.do_de_serialize()
        node.right = self.do_de_serialize()

        return node
            
