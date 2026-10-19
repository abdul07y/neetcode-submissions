class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        li=[]
        for x in nums:
            if x not in li:
                li.append(x)
            else:
                return True
        return False
        