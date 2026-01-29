class Solution:
    def reverse(self, x: int) -> int:
        num=abs(x)
        result=0
        while num!=0:
            remainder=num%10
            result=result*10+remainder
            num//=10
        if result>2**31:
            return 0
        return result*(-1) if x<0 else result