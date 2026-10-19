class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicti={}
        op=[]
        for i in nums:
            dicti[i]=1+dicti.get(i,0)
        for j in range(k):
            temp=max(dicti,key=dicti.get)
            op.append(temp)
            del dicti[temp]
        return op