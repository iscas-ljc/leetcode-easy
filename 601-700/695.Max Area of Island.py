class Solution(object):
    def maxAreaOfIsland(self, grid):
        m, n = len(grid), len(grid[0])
        #计算矩阵长度
        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j]:
                grid[i][j] = 0
                #把中间点置0不会无限循环重复添加
                return 1 + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i + 1, j) + dfs(i, j - 1)
            return 0

        areas = [dfs(i, j) for i in range(m) for j in range(n) if grid[i][j]]
        return max(areas) if areas else 0