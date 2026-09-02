class Solution:
    def countDistinct(self, arr, k):
        sol={}
        res=[]
        for i in range(k):
            sol[arr[i]]=sol.get(arr[i],0)+1
        res.append(len(sol))
        for i in range(k,len(arr)):
            sol[arr[i]]=sol.get(arr[i],0)+1
            sol[arr[i-k]]=sol.get(arr[i-k])-1
            if sol[arr[i-k]]==0:
                del sol[arr[i-k]]
            res.append(len(sol))
        return res
            
