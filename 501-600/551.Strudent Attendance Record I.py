class Solution(object):
    def checkRecord(self, s):
        if s.count('A')>1 or 'LLL' in s:
            return False
        return True