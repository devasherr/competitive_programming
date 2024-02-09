class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    
    def doUnion(self,a,n,b,m):
        a = set(a)
        b = set(b)
        c = a | b
        
        count = 0
        for n in c:
            count += 1
        return count
