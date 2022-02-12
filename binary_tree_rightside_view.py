# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        lvl_dic={}
        visited=[]
        def dfs(root,h):
            if root:
                if root not in visited:
                    visited.append(root)
                    lvl_dic[h]=root.val
                    dfs(root.left,h+1)
                    dfs(root.right,h+1)
        
        dfs(root,0)
        
        res=[]
        for val in lvl_dic.values():
            res.append(val)
        
        return res
