class Solution(object):
    def islandPerimeter(self, grid):
    	lenx=len(grid)
    	if grid[0] is not None:
    		leny=len(grid[0])
    	result=0
    	for i in range(lenx):
    		for j in range(leny):
    			if grid[i][j]==1:
    				result+=4
    				if i>0 and grid[i-1][j]==1:
    					result-=2
    				if j>0 and grid[i][j-1]==1:
    					result-=2
    	return result
#有一个1加4，有一个相邻减2
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        