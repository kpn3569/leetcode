class Solution:
    def climbStairs(self, n: int) -> int:
        n1=1
        n2=2
        if n1==n:
            return n1
        if n==n2:
            return n2
        for i in range(2,n):
            n3=n1+n2
            n1=n2
            n2=n3
        
        return n3
