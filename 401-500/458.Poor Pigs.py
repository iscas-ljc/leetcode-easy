class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        return int(math.ceil(math.log(buckets, 1 + minutesToTest / minutesToDie)))
        