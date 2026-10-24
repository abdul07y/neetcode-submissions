class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        col=Counter(nums)
        res=[]
        for key in col:
            if col[key]>len(nums)/3:
                res.append(key)
        return res