# O(N) Time, O(1) Space      
# Draw back in this problem is that if N is very large which create numeric problem OR ""OverFlow Problem""
def find_missing_num(arr, n):
    sum = (n*(n+1)/2)
    for i in arr:
        sum -= i
    return sum

# O(N) Time, O(1) Space 
# In this we are not summing up N, which will not create numeric problem Or ""NO OverFlow Problem""
# we are using XOR in this solution
def findMissingNum(a,n):
    x1 = a[0] 
    x2 = 1
    
    for i in range(1, n): 
        x1 = x1 ^ a[i]      #We are doing XOR of the array elements
    
    for i in range(2, n + 2): 
        x2 = x2 ^ i        #Now we are applying the xor operation on indices 
    return x1 ^ x2          #If you apply XOR of the x1 and x2 then you get the missing number

if __name__=='__main__':
    l=[1,2,3,5] # Their should me only one missing number
    n=len(l)
    print(find_missing_num(l, n+1)) # O(N) Time, O(1) Space
    miss=findMissingNum(l,n)  #O(N) TIme, O(1) Space
    print(miss)

