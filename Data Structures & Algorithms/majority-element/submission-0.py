class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic={}
        maxi=0
        for i in nums:
            if i not in dic:
                dic[i]=nums.count(i)
        result=max(dic,key=dic.get)
        return int(result)