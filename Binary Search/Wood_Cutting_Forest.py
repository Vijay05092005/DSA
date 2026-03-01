class Solution:
    def find_height(self,tree,n,k):
        l=0
        h=max(tree)
        while l <= h:
            m=(l+h)//2
            wood=0
            for i in range(0,len(tree)):
                if tree[i] > m:
                    wood+=(tree[i]-m)
            if wood == k:
                return m
            elif wood > k:
                l=m+1
            else:
                h=m-1
        return -1
