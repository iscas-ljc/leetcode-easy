class Solution(object):
    def detectCapitalUse(self, word):
        if word.islower()==True or word.isupper()==True or word.istitle():
            return True
        return False