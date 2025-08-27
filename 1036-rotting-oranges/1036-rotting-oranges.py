class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n= len(grid), len(grid[0])
        queue =deque()
        fresh =0
        mint =0
        for i in range(m):
            for j in range(n):
                if grid[i][j] ==2:
                    queue.append((i, j))
                elif grid[i][j]== 1:
                    fresh += 1
        d= [(-1,0),(1,0),(0,-1),(0,1)]
        while queue and fresh > 0:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in d:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx<m and 0<= ny<n and grid[nx][ny] == 1:
                        grid[nx][ny]= 2
                        fresh -=1
                        queue.append((nx,ny))
            if queue:  
                mint += 1
        return mint if fresh == 0 else -1