class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a=0
        for i in digits:
            a=(a*10)+i
        l=[]
        a+=1
        while(a>0):
            l.append(int(a%10))
            a=(a//10)
        return l[::-1]
