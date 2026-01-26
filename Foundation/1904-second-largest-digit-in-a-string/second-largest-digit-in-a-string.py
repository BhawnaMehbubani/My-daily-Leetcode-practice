class Solution:
    def secondHighest(self, s: str) -> int:
        arr=set()
        for char in s:
            if(char.isdigit()):
                arr.add(int(char))
        if(len(arr)<2):
            return -1
        arr=sorted(arr)
        return arr[-2]

        