class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        single_value = 0        

        for number in nums:       
            single_value ^= number  
        return single_value