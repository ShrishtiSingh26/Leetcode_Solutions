# Last updated: 7/5/2026, 7:41:34 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # Step 1: inorder traversal to collect sorted values
        arr = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)
        
        inorder(root)
        
        
        # Step 2: build balanced BST from sorted array
        def build(l, r):
            if l > r:
                return None
            
            mid = (l + r) // 2
            node = TreeNode(arr[mid])
            
            node.left = build(l, mid - 1)
            node.right = build(mid + 1, r)
            
            return node
        
        return build(0, len(arr) - 1)
