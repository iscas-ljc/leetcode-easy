class MinStack(object):

    def __init__(self):
        self.a=[]
        

    def push(self, x):
        nowmin=self.getMin()
        if nowmin==None or nowmin>x:
            nowmin=x
        self.a.append((x,nowmin))

    def pop(self):
        self.a.pop()
        

    def top(self):
        if len(self.a)==None:
            return None
        else:
            return self.a[len(self.a)-1][0]

        

    def getMin(self):
        if len(self.a)==None:
            return None 
        else:
            return self.a[len(self.a)-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()