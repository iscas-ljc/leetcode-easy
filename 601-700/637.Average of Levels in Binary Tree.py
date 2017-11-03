class Solution(object):
    def averageOfLevels(self, root):
        #层序遍历，用newlayer更新layer
        #直到叶子节点下一层为None
        #跳出while
        result=[]
        layer=[root]
        while layer:
            result.append(1.0*sum([n.val for n in layer])/len(layer))
            #计算每一行平均值
            newlayer=[]
            for n in layer:
                if n.left is not None:
                    newlayer.append(n.left)
                if n.right is not None:
                    newlayer.append(n.right)
            layer=newlayer
        return result 