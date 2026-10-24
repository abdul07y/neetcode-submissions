class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        seen=list(set(nums))
        res=[]
        n=len(nums)
        for i in seen:
            if nums.count(i)>n/3:
                res.append(i)
        return res
        