class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Initialize
        max_prod = nums[0]
        min_prod = nums[0]
        result = nums[0]

        # Traverse array
        for i in range(1, len(nums)):
            num = nums[i]

            # If number is negative, swap
            if num < 0:
                max_prod, min_prod = min_prod, max_prod

            # Update max and min product
            max_prod = max(num, max_prod * num)
            min_prod = min(num, min_prod * num)

            # Update result
            result = max(result, max_prod)

        return result