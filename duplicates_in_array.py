class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d=dict()
        for n in nums:
            if n in d.keys():
                return True
            else:
                d[n]=1
                
        return False
