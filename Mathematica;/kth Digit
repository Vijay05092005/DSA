class Solution:
    def kthDigit(self, a, b, k):
        c=a**b
        ld=c%10
        c=c//10
        counter=1
        while counter!=k:
            ld=c%10
            c=c//10
            counter+=1
        return ld
