class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n=len(nums)
        li=[1]*n
        prefix=1
        for i in range(n):
            li[i]=prefix
            prefix*=nums[i]
        postfix=1
        for j in range(n-1,-1,-1):
            li[j]*=postfix
            postfix*=nums[j]
        return li