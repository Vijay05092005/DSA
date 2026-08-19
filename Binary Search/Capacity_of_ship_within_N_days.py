class Solution(object):
    def shipWithinDays(self, weights, days):
        l=max(weights)
        h=sum(weights)
        while l <= h:
            m=(l+h)//2
            su=0
            day=1
            for i in range(len(weights)):
                if weights[i]+su <= m:
                    su+=weights[i]
                else:
                    day+=1
                    su=weights[i]
            if day <= days:
                sol=m
                h=m-1
            else:
                l=m+1
        return sol
