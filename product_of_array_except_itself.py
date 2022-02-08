class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref=[1]*len(nums)
        post=[1]*len(nums)
        for i in range(len(nums)-1):
            pref[i+1]=pref[i]*nums[i]
        for i in range(len(nums)-1,0,-1):
            post[i-1]=post[i]*nums[i]
        for i in range(len(nums)):
            pref[i]=pref[i]*post[i]
        return pref
