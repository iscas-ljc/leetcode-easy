class Solution(object):  
    def generate(self, numRows):  
        """ 
        :type numRows: int 
        :rtype: List[List[int]] 
        """  
        triangle = []  
        for i in range(numRows):  
            row = [1]  
            if i == 0:  
                triangle.append(row)  
                continue  
            for j in range(1, i):  
                num = triangle[i-1][j-1] + triangle[i-1][j]  
                row.append(num)  
            row.append(1)  
            triangle.append(row)  
        return triangle  
