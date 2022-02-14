class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        num_island=0
        rows,cols=len(grid),len(grid[0])
        
        visited=set()
        
        def bfs(r,c):
            
            queu=list()
            queu.append((r,c))
            visited.add((r,c))
            while queu:
                row,col=queu.pop(0)
                direction=[[1,0],[-1,0],[0,1],[0,-1]]
                
                for dr,dc in direction:
                    r,c=row+dr,col+dc
                    if (r,c) not in visited and r in range(rows) and c in range(cols) and grid[r][c]=='1':
                        queu.append((r,c))
                        visited.add((r,c))
        
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1' and (r,c) not in visited:
                    bfs(r,c)
                    num_island+=1
        
        
        return num_island
