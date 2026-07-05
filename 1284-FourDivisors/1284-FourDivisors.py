# Last updated: 7/5/2026, 7:41:37 PM
class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import math
        
        def four_divisor_sum(n):
            divs = set()
            for i in range(1, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    divs.add(i)
                    divs.add(n // i)
                    if len(divs) > 4:
                        return 0
            return sum(divs) if len(divs) == 4 else 0
        
        total = 0
        for num in nums:
            total += four_divisor_sum(num)
        
        return total
