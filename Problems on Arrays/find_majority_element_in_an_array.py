## O(N^2) Time, O(1) Space
def getMajority_Without_Hash(arr):
    l = list()
    maxVal = 0
    maxCount = 1
    for i in arr:
        count = 0    
        for j in arr:
            if i == j:
                count += 1
        if i not in l:
            if count > maxCount:
                maxVal = i
                maxCount = count
                l = list()
                l.append(i)
            elif count == maxCount:
                l.append(i)
    return l

## O(N) Time, O(N) Space
def getMajority_With_Hash(arr):
    countDict = dict()
    for i in arr:
        if i in countDict:
            countDict[i] = countDict[i] + 1
        else:
            countDict.update({i : 1})
    l = list()
    maxVal = 0
    key = 0
    for k, v in countDict.items():
        if v > maxVal:
            key = k
            maxVal = v
            l = list()
            l.append(key)
        elif maxVal == v:
            l.append(k)
    return l


## Condition if Majority greater equal to Half of the N 
## O(N) Time, O(1) Space
def findMajority(arr, n):
    m_element = 0 # Majority Number
    count = 1 
    for i in range(n):
        if arr[i] == m_element:
            count += 1
        else:
            count -= 1
        if count == 0:
            m_element = arr[i]
            count += 1
    return m_element


def isMajority(arr, n, m_element):
    count = 0
    for i in range(n):
        if arr[i] == m_element:
            count += 1
    if count >= n/2:
        return True, count
    else:
        return False, count


if __name__=='__main__':
    arr=[3, 3, 4, 2, 4, 4, 2, 4, 3, 2, 3, 2, 2, 2]
    print("Length: ", len(arr))
    # O(N^2) Time, O(1) Space
    print("O(N^2) Time, O(1) Space: ", getMajority_Without_Hash(arr))
    
    # O(N) Time, Theta(N) Space
    print("O(N) Time, Theta(N) Space: ", getMajority_With_Hash(arr))
    
    # O(N) Time, O(1) Space
    value=findMajority(arr,len(arr))
    val = isMajority(arr,len(arr),value)
    if(val[0]):
        print("O(N) Time, O(1) Space: ", value, val[1])
    else:
        print("Majority Element Is Less Then N/2, length is: ", val[1])
