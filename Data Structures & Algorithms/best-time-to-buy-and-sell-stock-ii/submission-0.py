class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        profit=0
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                profit+=nums[i+1]-nums[i]
            else:
                continue
        return profit

