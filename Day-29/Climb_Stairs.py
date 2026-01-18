class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Two variables to store previous values
        prev2 = 1   # ways for step 1
        prev1 = 2   # ways for step 2
        
        # Calculate for step 3 to n
        for i in range(3, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        
        return prev1