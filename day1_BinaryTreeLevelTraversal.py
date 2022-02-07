class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        store=dict()
        ans=[]
        self.dfs(root,0,store)
        for _,value in store.items():
            ans.append(value)
        return ans
    
    def dfs(self,root,level,store):
        if root:
            if level in store.keys():
                store[level]=store[level]+[root.val]
            else:
                store[level]=[root.val]
                
            self.dfs(root.left,level+1,store)
            self.dfs(root.right,level+1,store)
