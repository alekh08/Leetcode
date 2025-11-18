class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
# ---------------- Approach 1 --------------- #
        # Greedy Scan
        # c=0
        # a=0
        # n=len(bits)
        # while a<n:
        #     if bits[a]==0:
        #         a+=1
        #         c=1
        #     else:
        #         a+=2
        #         c=0
        # if c==1:
        #     return True
        # else:
        #     return False

# ---------- 2nd Appproach ----------- #
        # count trailing 1's
        i=len(bits)-2
        c=0
        while i>=0 and bits[i]==1:
            c+=1
            i-=1
        return c%2==0
