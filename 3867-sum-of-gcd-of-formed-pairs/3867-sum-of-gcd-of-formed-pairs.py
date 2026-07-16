class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefix_gcd = []
        max_so_far = 0
        
        # 1. Build the prefix GCD array
        for num in nums:
            max_so_far = max(max_so_far, num)
            prefix_gcd.append(math.gcd(num, max_so_far))
            
        # 2. Sort the prefix GCD array
        prefix_gcd.sort()
        
        # 3. Pair up smallest and largest, and sum their GCDs
        total_gcd_sum = 0
        left, right = 0, len(prefix_gcd) - 1
        
        while left < right:
            total_gcd_sum += math.gcd(prefix_gcd[left], prefix_gcd[right])
            left += 1
            right -= 1
            
        return total_gcd_sum