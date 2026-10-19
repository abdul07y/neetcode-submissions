class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res,mcount=0,0
        count={}
        for i in nums:
            count[i]=1+count.get(i,0)
            res=i if count[i]>mcount else res
            mcount=max(count[i],mcount)
        return res