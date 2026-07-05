# Last updated: 7/5/2026, 7:41:20 PM
class Solution(object):
    def maxProduct(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        MOD = 10**9 + 7
        self.max_prod = 0

        # Step 1: compute total sum of tree
        def totalSum(node):
            if not node:
                return 0
            return node.val + totalSum(node.left) + totalSum(node.right)

        total = totalSum(root)

        # Step 2: postorder traversal to compute subtree sums
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            subtree_sum = node.val + left + right

            # consider splitting here
            self.max_prod = max(
                self.max_prod,
                subtree_sum * (total - subtree_sum)
            )

            return subtree_sum

        dfs(root)
        return self.max_prod % MOD