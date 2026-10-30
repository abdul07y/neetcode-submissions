class Solution:
    def isPalindrome(self, s: str) -> bool:
      
        s1=s.replace(" ","")
        s2=""
        for x in s1:
            if x in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
                s2+=x
        s2=s2.lower()
        l=0
        r=len(s2)-1
        while(l<r):
            if s2[l]!=s2[r]:
                return False
            l+=1
            r-=1
        return True