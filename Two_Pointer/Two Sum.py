class Solution:
	def twoSum(self, arr, target):
		arr.sort()
		i=0
		j=len(arr)-1
		while i < j:
		    if arr[i]+arr[j] == target:
		        return True
		    elif arr[i]+arr[j] > target:
		        j-=1
		    else:
		        i+=1
		return False
		
