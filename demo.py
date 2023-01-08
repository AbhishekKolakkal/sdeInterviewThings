from audioop import reverse
from curses.ascii import islower
from hashlib import new
# from imp import new_module
from math import floor
from unittest import result


def majorityEle(A):

    n = len(A)

    checkFreq = floor(n/3)

    new_dict = {}

    maxResult = float('-inf')

    ret = 0

    for i in A:
        if (i not in new_dict):
            new_dict[i] = 1
        else:
            new_dict[i] = new_dict[i] + 1

    # print(new_dict)

    for j in new_dict.keys():
        # print("sjnbdjd", new_dict[j])
        if new_dict[j] > maxResult:
            maxResult = new_dict[j]
            # print("maxResult", maxResult)
            ret = j

    # print(new_dict)
    # print(ret)
    if new_dict[ret] > checkFreq:
        return ret
    else:
        return -1 




def magicNumber(A):
    binaryNumStr = bin(A).replace("0b", "")
    

    binaryNumInt = int(binaryNumStr)

    b = binaryNumInt >> 1

    print(b)
    

    
def excelColumnNumber(A):
    # print(len(A))
    res = 0
    raiseTO = 0
    for i in range(len(A) - 1, -1, -1):
        digit = (ord(A[i]) - ord('A') + 1)
        # print(pow(26, 1))
        res = res + (digit * pow(26, raiseTO))
        # print(res)
        raiseTO = raiseTO + 1
        # print(res)
    return res
        

def moduloOperation(A, B):
    # res = 0
    if A == B:
        return A 
    
    if A > B:
        return A - B

    if B > A:
        return B - A    



# def reverseString(A):
#     reverseString = ''
#     for i in reversed(A):
#         reverseString += i
    
#     return reverseString


# def longestPalindrome(A):
#     maxPalindrome = ""
#     maxPalindromeNum = 0
#     left = 0
#     right = 0
#     for i in range(len(A)):
#         while(left <= 0 and right <= len(A)):
#             print(left, right)
#             if A[left] == A[right]:
#                 left -= 1
#                 right += 1
                
#             if maxPalindromeNum > (right - left):
#                 maxPalindrome = A[left:right]
#     print(maxPalindrome)



# A = "aaaabaaa"

# longestPalindrome(A)


# A = "abhishek"
# print(A[0:4])



def rotateRight(a, n):
    ret = []
    for i in range(len(a)):
        index = (i + n) % len(a)
        ret.append(a[index])
    print(ret)


# A = [1, 2, 3, 4]
# B = 2

A = [1, 2, 2]
B = 3
rotateRight(A, B)


def reverseArray(A):
    ret = []
    lengthOfArray = len(A)

    for i in range(lengthOfArray -1, -1, -1):
        print(i)
        ret.append(A[i])
    
    print(ret)


def littlePonny(A, N):
    count = 0
    checkNum = 0
    for j in A:
        if j == N:
            checkNum = checkNum + 1

    if checkNum == 0:
        print("In the checkNum block")
        return -1
    
    for i in A:
        if i > N:
            count = count + 1

    if count == 0:
        print("In if block",count)
        return -1
    else:
        print("In else block", count)
        return count 




def secondLargest(A):
    LargestIdx = -1
    secondLargestIdx = -1
    maxNumber = float('-inf')
    secondMaxNumber = float('-inf')
    if len(A) < 2:
        return -1
    
    for i in range(len(A)):
        if A[i] > maxNumber:
            maxNumber = A[i]
            LargestIdx = i 
    
    print("hello", maxNumber, LargestIdx)

    for j in range(len(A)):
        # print("ndjbd", j, LargestIdx, j != LargestIdx and A[j] > secondMaxNumber and A[j] <= maxNumber)
        if j != LargestIdx:
            secondMaxNumber = max(secondMaxNumber, A[j])

    print(secondMaxNumber)
        
    

def maxMin(A):
    maxEven = float('-inf')
    minOdd = float('inf')
    ans = 0
    for i in A:
        # print(i)
        if i % 2 == 0:
            maxEven = max(i, maxEven)
        else:
            minOdd = min(i, minOdd)
    # print(maxEven, minOdd)
    print((maxEven - minOdd))
    return (maxEven - minOdd)



def armsStrongNumbers(N):
    sum = 0

    for i in range(1, N):
        while i > 0:
            digit = i % 10
            sum = sum + digit**3
            i = i // 10

        if i == sum:
            print(sum)
        else:
            print(i, "Not an armstron number")    





def minMaxArray(A):
    minNum = float('inf')
    maxNum = float('-inf')

    for i in A:
        if i > maxNum:
            maxNum = max(maxNum, i)


    for j in A:
        if j < minNum:
            minNum = min(minNum, j)


    print(maxNum, minNum)




def goodPair(A, B):
    for i in range(0, len(A)):

        for j in range(i + 1, len(A)):
            print(A[i], A[j])
            if A[i] + A[j] == B:
                print("sjbskj", A[i], A[j])
            else:
                return 0



