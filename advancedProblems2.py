from re import A, L
import math
import re
from traceback import print_tb

def binarySearch(A, B):
    l = 0
    r = len(A) - 1
    while(l <= r):
        mid = (l + r)//2
        if A[mid] == B:
            return mid
        elif A[mid] > B:
            r = mid - 1
        else:
            l = mid + 1
    return mid
    

# A = [1, 3, 5, 6]
# B = 5

# A = [1]
# B = 1

# print(binarySearch(A, B))

def peakElement(A):
    l = 1
    r = len(A) - 2

    while(l <= r):
        mid = (l + r)//2

        if(A[mid] >= A[mid + 1]) and A[mid] >= A[mid + 1]:
            return A[mid]
        if A[mid - 1] > A[mid]:
            r = mid - 1
        if A[mid + 1] > A[mid]:
            l = mid + 1
    
    if A[0] > A[len(A) - 1]:
        return A[0]
    else:
        return A[len(A) - 1]



# A = [1, 2, 3, 4, 5]
# A = [5, 17, 100, 11]
# A = [ 1, 1000000000, 1000000000]
# print(peakElement(A))


def rotatedSortedArraySearch(A, B):
    l = 0
    r = len(A) - 1
    while (l <= r):
        m = (l + r)//2

        if A[m] == B:
            return m

        if (B >= A[l] and B <= A[m]):
            r = m - 1
        
        if (B >= A[m] and B <= A[r]):
            l = m + 1

    return -1



# A = [ 101, 103, 106, 109, 158, 164, 182, 187, 202, 205, 2, 3, 32, 57, 69, 74, 81, 99, 100 ]
# B = 202

# A = [ 180, 181, 182, 183, 184, 187, 188, 189, 191, 192, 193, 194, 195, 196, 201, 202, 203, 204, 3, 4, 5, 6, 7, 8, 9, 10, 14, 16, 17, 18, 19, 23, 26, 27, 28, 29, 32, 33, 36, 37, 38, 39, 41, 42, 43, 45, 48, 51, 52, 53, 54, 56, 62, 63, 64, 67, 69, 72, 73, 75, 77, 78, 79, 83, 85, 87, 90, 91, 92, 93, 96, 98, 99, 101, 102, 104, 105, 106, 107, 108, 109, 111, 113, 115, 116, 118, 119, 120, 122, 123, 124, 126, 127, 129, 130, 135, 137, 138, 139, 143, 144, 145, 147, 149, 152, 155, 156, 160, 162, 163, 164, 166, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177 ]
# B = 42
# print(rotatedSortedArraySearch(A, B))

def squareRootUsingBinarySearch(A):
    l = 1
    r = A
    result = 1
    while l <= r:
        middle = (l + r)//2
        if (middle*middle == A):
            return middle
        elif (middle*middle) > A:
            r = middle - 1
        elif (middle*middle) < A:
            result = middle
            l = middle + 1
    
    return result


    return 0


# A = 11
# A = 9
# print(squareRootUsingBinarySearch(A))



def specialIntegerUsingBinarySearch(A, B):
    left = 0
    right = len(A) -1
    result = 0
    while (left <= right):
        middle = (left + right)//2

        if (checkMaximumWithSlidingWindow(A, middle, B)):
            result = middle
            left = middle + 1
        else: 
            right = middle - 1
    return result

def checkMaximumWithSlidingWindow(A, middle, target):
    i = 0
    j = middle - 1
    ans = 0
    while (j < len(A)):
        sum = 0
        
        for k in range(i, (j + 1)):
            sum = sum + A[k]

        ans = max(ans, sum)

        i += 1
        j += 1
    
    if ans <= target:
        return True
    else:
        return False


# A = [1, 2, 3, 4, 5]
# B = 10

# A = [5, 17, 100, 11]
# B = 130
# print(specialIntegerUsingBinarySearch(A, B))


# Python program to find LCM of two numbers
 
# # Recursive function to return gcd of a and b
# def gcd(a,b):
#     if a == 0:
#         return b
#     return gcd(b % a, a)
 
# # Function to return LCM of two numbers
# def lcm(a,b):
#     return (a / gcd(a,b))* b
 
# # Driver program to test above function
# a = 2
# b = 3
# print('LCM of', a, 'and', b, 'is', lcm(a, b))
 
# # This code is contributed by Danish Raza


def paintersPartition(A, B, C):
    for i in range(0, len(C)):
        C[i] = C[i] * B
    
    l = 1

    i = 0
    arraySum = 0
    for i in range(0, len(C)):
        arraySum = arraySum + C[i]
    
    
    r = arraySum
    result = 0
    while(l <= r):
        m = (l + r)//2

        if(checkForSatisfaction(C, A, m)):
            result = m
            r = m - 1
        else:
            l = m + 1
        
    return (result%10000003)


def checkForSatisfaction(C, A, m):
    i = 0
    maximumArrayValue = float('-inf')

    for i in range(0, len(C)):
        maximumArrayValue = max(maximumArrayValue, C[i])
    
    if maximumArrayValue > m:
        return False

    countOfWorkers = 1
    sum = 0
    i = 0
    for i in range(0, len(C)):
        sum = sum + C[i]
        if (sum > m):
            countOfWorkers += 1
            sum = C[i]
    
    if (countOfWorkers <= A):
        return True
    return False

# A = 2
# B = 5
# C = [1, 10]

# A = 10
# B = 1
# C = [1, 8, 11, 3]

# print(paintersPartition(A, B, C))


def aggressiveCows(A, B):
    left = A[0]
    right = A[len(A) - 1]
    ans = 0
    while (left <= right):
        middle = (left + right)//2
        if(checkForDistance(A, B, middle)):
            ans = middle
            left = middle + 1
        else:
            right = middle - 1
    return ans

def checkForDistance(A, B, middle):
    cowCount = 1
    previousPositionOfCow = A[0]
    i = 1

    while(i < len(A)):        
        result = A[i] - previousPositionOfCow

        if(result < middle):
            i += 1
        else:
            cowCount += 1
            previousPositionOfCow = A[i]
    
    if cowCount >= B:
        return True
    else:
        return False



def checkForDistance(A, B, middle):
    cowCount = 1
    previousPositionOfCow = A[0]
    i = 1

    while(i < len(A)):        
        result = A[i] - previousPositionOfCow

        if(result >= middle):
            cowCount += 1
            previousPositionOfCow = A[i]

        if(cowCount == B):
            return True

        i += 1

    return False  


# A = [1, 2, 3, 4, 5]
# B = 3

# A = [1, 2]
# B = 2
# print(aggressiveCows(A, B))



def subArrayWithGivenSum(A, B):
    if len(A) == 0:
        return [-1]
    
    if len(A) == 1 and A[0] == B:
        return [A[0]]
    
    p1 = 0
    p2 = 1

    while (p1 < len(A) and p2 < len(A)):
        res = slidingWindowCheck(A, p1, p2)

        if (res == B):
            return A[p1:p2+1]
        if (res < B):
            p2 += 1
        if (res > B):
            p1 += 1
            p2 = p1 + 1
    
    return [-1]

def slidingWindowCheck(A, p1, p2):
    sum = 0
    for i in range(p1, (p2 + 1)):
        sum = sum + A[i]
    
    return sum


# A = [1, 2, 3, 4, 5]
# B = 5

# A = [5, 10, 20, 100, 105]
# B = 110
# print(subArrayWithGivenSum(A, B))



def pairWithGivenDifference(A, B):
    hashSet = set()
    A.sort()
    p1 = 0
    p2 = 1
    while(p1 < len(A) and p2 < len(A)):
        res = A[p2] - A[p1]

        if (res == B):
            hashSet.add(tuple([A[p1], A[p2]]))   
            p1 += 1
            p2 += 1
        if (res < B):
            p2 += 1
        if (res > B):
            p1 += 1
            p2 = p1 + 1
        
    return len(hashSet)


# A = [1, 5, 3, 4, 2]
# B = 3

# A = [8, 12, 16, 4, 0, 20]
# B = 4

# A = [1, 1, 1, 2, 2]
# B = 0

# print(pairWithGivenDifference(A,B))


def containerWithMostWater(A):
    if len(A) == 0 or len(A) == 1:
        return 0
    
    res = 0
    p1 = 0
    p2 = len(A) - 1

    while (p1 < p2):
        ans = abs(A[p2] - A[p1]) * min(A[p1], A[p2])
        res = max(res, ans)

        if (A[p1] < A[p2]):
            p1 += 1
        
        if (A[p1] > A[p2]):
            p2 -= 1
        
        if (A[p1] == A[p2]):
            p1 += 1
            p2 -= 1
    
    return res



# A = [1, 5, 4, 3]
# A = [1]
# print(containerWithMostWater(A))

def threeSumZero(A):
    A.sort()
    res = []

    for i in range(0, (len(A) - 2)):
        p1 = i + 1
        p2 = len(A) - 1

        while (p1 < p2):
            sum = A[i] + A[p1] + A[p2]
            if (sum == 0):
                if [A[i], A[p1], A[p2]] not in res:
                    res.append([A[i], A[p1], A[p2]])
            
            if (sum > 0):
                p2 -= 1
            else:        
                p1 += 1
    
    return res

            


# A = [-1,0,1,2,-1,4]
# print(threeSumZero(A))



def pairWithGivenSum(A, B):
    # hashSet = set()
    count = 0
    A.sort()
    p1 = 0
    p2 = 1
    while(p1 < len(A) and p2 < len(A)):
        res = A[p2] + A[p1]
        if (res == B):
            count += 1
            p1 += 1
            p2 += 1
        if (res < B):
            p2 += 1
        if (res > B):
            p1 += 1
            p2 = p1 + 1
        
    return count


# A = [1, 1, 1]
# B = 2

# A = [1, 1]
# B = 2
# print(pairWithGivenSum(A, B))


def longestConsecutiveSequece(A):
    hashSet = set(A)
    result = 1

    for value in hashSet:
        if (value - 1) not in hashSet:
            count = 1
            i = value + 1
            while i in hashSet:
                count = count + 1
                i = i + 1
                result = max(result, count)
    print(result)
    return result

# A = [100, 4, 200, 1, 3, 2]
# A = [2, 1]
# longestConsecutiveSequece(A)

def shaggyAndDistance(A):
    hash = {}
    minValue = float('inf')

    for i in range(0, len(A)):
        if A[i] not in hash:
            hash[A[i]] = i
        else:
            value = i - hash[A[i]]
            minValue = min(minValue, value)
            hash[A[i]] = i
    if minValue == float('inf'):
        return -1
    
    return minValue


# A = [7, 1, 3, 4, 1, 7]
# A = [1, 1]
# shaggyAndDistance(A)


def subArrayWithZeroSum(A):
    ps = [0]*len(A)

    ps[0] = A[0]
    for i in range(1, len(A)):
        ps[i] = A[i] + ps[i - 1]

    for i in range(0, len(ps)):
        if ps[i] == 0:
            return 1

    hash = {}
    i = 0

    for i in range(0, len(ps)):
        if ps[i] not in hash:
            hash[ps[i]] = 1
        else:
            hash[ps[i]] += 1
    
    i = 0
    for i in hash.values():
        if i > 1:
            return 1

    return 0


A = [2,2,1,-3,4,3,1,-8,6,-2,-1]
# A = [1, 2, 3, 4, 5]
# A = [-1, 1]
print(subArrayWithZeroSum(A))