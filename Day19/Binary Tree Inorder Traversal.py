class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res = []
        self.helper(root, res)
        return res
    
    def helper(self, node, res):
        if not node:
            return
        
        # Traverse left subtree
        self.helper(node.left, res)
        
        # Visit the root
        res.append(node.val)
        
        # Traverse right subtree
        self.helper(node.right, res)
