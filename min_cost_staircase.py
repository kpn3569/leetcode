class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost=[0]*(len(cost)+1) #tabular or buttom to top approach
        for i in range(2,len(cost)+1): #since we can start from 0 and 1 so cost is 0
            one_hop=cost[i-1]+min_cost[i-1]
            two_hop=cost[i-2]+min_cost[i-2]
            min_cost[i]=min(one_hop,two_hop)
        
        return min_cost[-1]
