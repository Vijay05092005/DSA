class Solution:
    def minAnd2ndMin(self, arr):
        s=float('inf')
        for x in arr:
            if s > x:
                s=x
        ss=float('inf')
        for x in arr:
            if ss > x and x > s:
                ss=x
        if s==float('inf') or ss==float('inf'):
            return [-1]
        return[s,ss]
