class Solution:
    def longestKSubstr(self, s, k):
        maximum=-1
        a={}
        left=0
        for right in range(len(s)):
            a[s[right]]=a.get(s[right],0)+1
            while k < len(a):
                a[s[left]]=a.get(s[left])-1
                if a.get(s[left]) == 0:
                    del a[s[left]]
                left+=1
            if len(a)==k:
                maximum=max(maximum,right-left+1)
        return maximum
