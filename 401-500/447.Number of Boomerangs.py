class Solution(object):
    def numberOfBoomerangs(self, points):
        res = 0
        for p in points:
            cmap = {}
            for q in points:
                f = p[0]-q[0]
                s = p[1]-q[1]
                cmap[f*f + s*s] = 1 + cmap.get(f*f + s*s, 0)
            for k in cmap:
                res += cmap[k] * (cmap[k] -1)
        return res
#{}表示python中的dictionary
#get表示查找key，','后为没找到的返回值