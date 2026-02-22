class Solution(object):
    def rotateString(self, s, goal):
        for i in range(1,len(s)+1):
            a=s[i:]+s[:i]
            if goal==a:
                return True
        return False
