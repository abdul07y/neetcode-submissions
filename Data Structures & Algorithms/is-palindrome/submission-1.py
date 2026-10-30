class Solution:
    def isPalindrome(self, s: str) -> bool:
      
        s1=s.replace(" ","")
        s2=""
        for x in s1:
            if x.isalnum():
                s2+=x
        s2=s2.lower()
        return s2==s2[::-1]