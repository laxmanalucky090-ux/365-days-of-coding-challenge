class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # Step 1: If there are no houses
        if not nums:
            return 0
        
        # Step 2: If there is only one house
        if len(nums) == 1:
            return nums[0]
        
        # Step 3: Create dp array
        dp = [0] * len(nums)
        
        # Step 4: Base cases
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        # Step 5: Fill dp array
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        # Step 6: Return last value
        return dp[-1]