# Last updated: 7/5/2026, 7:41:44 PM
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def dfs(node):
            if not node:
                return (0, None)

            lh, lnode = dfs(node.left)
            rh, rnode = dfs(node.right)

            if lh == rh:
                return (lh + 1, node)
            elif lh > rh:
                return (lh + 1, lnode)
            else:
                return (rh + 1, rnode)

        return dfs(root)[1]
