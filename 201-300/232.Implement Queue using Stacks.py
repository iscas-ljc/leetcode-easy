class MyQueue(object):

    def __init__(self):
        self.instack=[]
        self.outstack=[]
        

    def push(self, x):
        self.instack.append(x)
        

    def pop(self):
        self.move()
        return self.outstack.pop()
        

    def peek(self):
        self.move()
        return self.outstack[-1]
        

    def empty(self):
        return (not self.instack) and (not self.outstack)

    def move(self):
        if not self.outstack: 
            while self.instack:
                self.outstack.append(self.instack.pop())