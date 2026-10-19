class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res,count=0,0
        for i in range(len(nums)):
            if count==0:
                res=nums[i]
            count+=(1 if nums[i]==res else -1)
        return res