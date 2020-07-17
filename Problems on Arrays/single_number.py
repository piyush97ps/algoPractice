# O(N^2) Time, O(1) Space
def getOddOccurence_with_bruteForce(arr):
    for i in range(len(arr)):
        cnt = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                cnt += 1
        if cnt%2 != 0:
            return arr[i]
    return -1

# O(N) Time and O(N) Space
def getOddOccurence_with_hashTable(arr):
    hashMap = dict()
    for i in arr:
        if i in hashMap:
            hashMap[i] = hashMap[i] + 1
        else:
            hashMap[i] = 1
        
    for k, v in hashMap.items():
        if v%2 != 0:
            return k
    
    return -1

# O(N) Time and O(1) Space, XOR : 1 ^ 1 = 0, 0 ^ 0 = 0, 1 ^ 0 = 1, 0 ^ 1 = 0
def getOddOccurence(arr):
    res=0
    for i in arr:
        res=res^i   # XOR
    return res


# there should be one number which has odd count
if __name__=='__main__':
    arr=[2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2]
    print(getOddOccurence_with_bruteForce(arr))
    print(getOddOccurence_with_hashTable(arr))
    print(getOddOccurence(arr))
