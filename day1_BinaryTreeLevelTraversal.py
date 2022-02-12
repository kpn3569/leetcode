class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
       visited=[]
        level={}
        def dfs(root,height):
            if root:
                if root not in visited:
                    visited.append(root)
                    if height not in level.keys():
                        level[height]=[root.val]
                    else:
                        level[height]=level[height]+[root.val]

                    dfs(root.left,height+1)
                    dfs(root.right,height+1)
        
        dfs(root,0)
        res=[]
        for val in level.values():
            res.append(val)
        
        return res
        
