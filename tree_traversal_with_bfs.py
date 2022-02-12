# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        visited=[]
        que=[]
        lvl={}
        def bfs(root):
            que.append([root,0])
            nd = que.pop(0)
            while nd[0]:
                if nd[0] not in visited:
                    visited.append(nd[0])
                
                    if nd[1] not in lvl.keys():
                        lvl[nd[1]]=[nd[0].val]
                    else:
                        lvl[nd[1]]=lvl[nd[1]]+[nd[0].val]
                    if nd[0].left:
                        que.append([nd[0].left,nd[1]+1])
                    if nd[0].right:
                        que.append([nd[0].right,nd[1]+1])


                if que:
                    nd=que.pop(0)
                else:
                    nd[0]=None
        
        bfs(root)
        res=[]
        for val in lvl.values():
            res.append(val)
        
        return res
