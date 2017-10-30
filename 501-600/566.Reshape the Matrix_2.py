    def matrixReshape(self, nums, r, c):
        l1=len(nums)
        l2=len(nums[0])
        a=[]
        result =[[0 for col in range(c)] for row in range(r)]
        #b=[0]*c
        #result=[]
        #for i in range(r):
        #    result.append(b)
        #这样初始化的数组都是一样的，改一个b[0]三个都会改
        if l1*l2!=r*c:
            return nums
        else:
            for i in range(l1):
                for j in range(l2):
                    a.append(nums[i][j])
            e=0
            for i in range(r):
                for j in range(c):
                    result[i][j]=a[e]
                    e+=1
        return result
