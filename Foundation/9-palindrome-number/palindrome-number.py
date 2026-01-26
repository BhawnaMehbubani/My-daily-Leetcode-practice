class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        num=x
        s=0
        while x!=0:
            n=x%10
            s=s*10+n
            x=x//10
        if s==num:
            return True
        return False
        