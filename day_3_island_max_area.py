class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        row = len(grid)
        col = len(grid[0])
        ans = 0
        visited = []

        def bfs(r, c):
            visited.append((r, c))
            que = [(r, c)]
            area = 1
            while que:
                rr, cc = que.pop(0)
                directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = rr + dr, cc + dc
                    if ((r, c) not in visited and r in range(row) and c in range(col) and grid[r][c] == 1):
                        visited.append((r, c))
                        que.append((r, c))
                        area += 1

            return area


        for r in range(row):
            for c in range(col):
                if ((r, c) not in visited and grid[r][c] == 1):
                    t=bfs(r, c)
                    ans = max(ans,t)
        return ans
