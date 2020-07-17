## Approach 1
def rotateOnce(arr,n):
    # O(N)
    temp = arr[n-1]
    for i in range(n-2, -1, -1):
        arr[i+1] = arr[i]
    arr[0] = temp

# O(N * K) time, where N is size of array and K is the number of rotation
def calling_K_Rotatinos(arr, n, k):
    for _ in range(k):
        rotateOnce(arr, n)
    print(arr)


## Approach 2
# O(N + K) time and O(K) Space, Where N is size of array and K is the number of rotation 
def shift_K_Elements(arr, n, k):
    arr = arr[k+1:n] + arr[0:k+1]
    print(arr)


## Approach 3
def reverse(arr,a,b):
    while(a<=b):
        temp=arr[a]
        arr[a]=arr[b]
        arr[b]=temp
        a+=1
        b-=1
 
# O(N) Time and O(1) Space, where N is size of array
def rotateKtimes(arr,n,k):
    reverse(arr,n-k,n-1)
    reverse(arr,0,n-k-1)
    reverse(arr,0,n-1)
    print(arr)


## Start
if __name__=='__main__':
    arr=[1,2,3,4,5,6,7]
    n = len(arr)
    calling_K_Rotatinos(list(arr), n, 3)
    shift_K_Elements(list(arr), n, 3)
    rotateKtimes(list(arr), n, 3)
