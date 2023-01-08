from cmath import inf
from re import A, I
from tabnanny import check
from unittest import result
# from tkinter import N
import math


def findCountOfSubSequence(A):
    #pseudo code
    '''
    1. write a for loop starting from the right
    2. count the number of G, if G is found then store in count
    3. If A is found then store the nummber o g in ans
    4. repeate this
    '''
    n = len(A)
    res = 0
    count_g = 0
    for i in range(n-1, -1, -1):
        if A[i] == 'G':
            count_g = count_g + 1
        if A[i] == 'A':
            res = res + count_g
        
    print(res)



def amazingSubString(A):
    n = len(A)
    res = 0
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    for i in range(n):
        if A[i] in vowels:
            sum = n - i
            res = res + sum

    return res        




def theLeaders(A):
    n = len(A)
    max = float('-inf')
    result = []
    for i in range(n -1, -1, -1):
        if A[i] > max:
            result.append(A[i])
            max = A[i]
    return result



def contigiousSubArray(A):
    maxSum = float('-inf')
    lengthOfArr = len(A)
    for s in range(lengthOfArr):
        # print(s)
        for e in range(s, lengthOfArr):
            currentSumm = maxSumOfArray(s, e, A, maxSum)
        maxSum = max(maxSum, currentSumm)
        return maxSum


def maxSumOfArray(s, e, A, maxSum):
    summ = 0
    for add in range(s, e):
        summ = summ + A[add]
    
    return summ
        # currentSum = maxSum + A[add]
        # if currentSum > maxSum:
            # maxSum = currentSum
            # print(currentSum) 
        



def subArraySum(A):
    temp, res = 0, 0
    for s in range(len(A)):
        temp = 0
        for e in range(s, len(A)):
           temp += A[e]
           res += temp
        
    
    print (res)
    
    # res = arraySum + res
    # print(res)



def additionOfTwoMatrices(A, B):
    # print(len(A[0]))
    res = []
    for i in range(len(A)):
        arbituaryArray = []
        for j in range(len(A[i])):
            arbituaryArray.append(A[i][j] + B[i][j])
        res.append(arbituaryArray)
    
    return res

# A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
# B = [[9, 8, 7],[6, 5, 4],[3, 2, 1]]
# additionOfTwoMatrices(A, B)



def antiDiagonal(A):
    res = []
    rowOfMatrix = 0
    columnOfMatrix = 0
    count = 0
    while(count <= len(A)):
        arbituaryArray = []
        while(columnOfMatrix >= 0 or rowOfMatrix <= (len(A) - 1)):
            count+=count
            arbituaryArray.append(A[rowOfMatrix][columnOfMatrix])
            rowOfMatrix += 1
            columnOfMatrix -= 1
            # print(rowOfMatrix, columnOfMatrix)
    arbituaryArray.append(0)    
    count+=1
    print(arbituaryArray)

    return 0



def columnSumOfMatrix(A):
    i = 0
    j = 0
    res = []


    while (j <= (len(A[i]) - 1)):
        sumOfColumns = 0
        while(i <= (len(A) - 1)):
            sumOfColumns += A[i][j]
            i += 1
        res.append(sumOfColumns)
        j += 1
        i = 0
    return res




def ifMatrixAreEqual(A, B):
    
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] != B[i][j]:
                return 1
    return 0



def matrixScalarProduct(A, B):

    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] = A[i][j] * B

    print(A)


def RowSumOfMatrix(A):
    res = []
    for i in range(len(A)):
        sumOfRow = 0
        for j in range(len(A[i])):
            sumOfRow += A[i][j]

        res.append(sumOfRow)        

    print(res)


def makeRowAndColumnZero(A):
    n = len(A)
    m = len(A[0])

    zr = dict()
    zc = dict()
    for i in range(0, n):
        for j in range(0, m):
            if(A[i][j] == 0):
                zr[i] = 0
                zc[j] = 0
            else:
                zr[i] = zr[i] if i in zr else 1
                zc[j] = zc[j] if j in zc else 1
    
    print(zr,zc)
    for i in range(0, n):
        for j in range(0, m):
            if(zr[i] == 0 or zc[j] == 0):
                A[i][j] = 0

    return A






def minorDiagonalSum(A):
    sum = 0

    for i in range(len(A)):
        sum = sum + A[i][(len(A) - 1 - i)]
    
    print(sum)
    return 0






def transposeOfAMatrix(A):
    i = 0
    j = 0
    while (i <= ((len(A)) -1)):
        j = i
        while(j <= ((len(A[i]) - 1))):
            temp = A[i][j]
            A[i][j] = A[j][i]
            A[j][i] = temp

            j += 1
        i += 1
    print(A)

def swap(A, i, j):
    temp = A[i][j]
    A[i][j] = A[j][i]
    A[j][i] = temp



def largestConsequtiveOnes(A):
    count = 0

    for i in range(0, (len(A) -1)):
        if A[i] == 0:
            left = i - 1
            right = i + 1
            count_left = 0
            count_right = 0
            while(left >= 0):
                if A[left] == 0:
                    break
                count_left += 1
                left -=1
            while(right < len(A)):
                if A[right] == 0:
                    break
                count_right +=1
                right +=1
            print(count_left, count_right)
            if count_left != 0 or count_right != 0:
                count = max(count, count_left + count_right + 1)
            else:
                count = max(count, count_left + count_right)
    print(count)






def christmasTrees(A, B):
    # flag = 0
    # ans = 0

    # for i in range(1, len(A)-1):

    #     minn = 0
    #     f = 0
    #     anss = B[i]
    #     for j in range(i-1, -1, -1):
    #         if(A[j] < A[i]):
    #             if f == 0:
    #                 f = 1
    #                 minn = B[j]
    #             else:
    #                 minn = min(minn, B[j])

    #     if(f == 0):
    #         continue

    #     anss += minn

    #     minn = 0
    #     f = 0

    #     for j in range(i+1, len(A)):
    #         if(A[j] > A[i]):
    #             if f == 0:
    #                 f = 1
    #                 minn = B[j]
    #             else:
    #                 minn = min(minn, B[j])

    #     if(f == 0):
    #         continue

    #     anss += minn

    #     if flag == 0:
    #         ans = anss
    #     else:
    #         ans = min(ans, anss)

    #     flag = 1

    # if(flag == 1):
    #     return ans
    # else:
    #     return -1













    res = float("inf")

    for j in range(1, (len(A))):
        best_left_value = float("inf")
        best_right_value = float("inf")
        minimum_value = B[j]

        for i in range((j-1), -1, -1):
            if A[i] < A[j] and B[i] < best_left_value:
                best_left_value = B[i]
        
        for k in range(j+1, len(A)):
            if A[k] > A[j] and B[k] < best_right_value:
                best_right_value = B[k]
        
        minimum_value = minimum_value + best_left_value + best_right_value
        print(minimum_value)
        print(i, j, k)
        res = min(res, minimum_value)
    print(res)


# A = [ 5, 9, 10, 4, 7, 8 ]
# B = [ 5, 6, 4, 7, 2, 5 ]
# christmasTrees(A, B)


# print(5 ^ 8)

def helpFromSam(N):
    count = 0

    while(N):
        count += N & 1
        N >>= 1
    print(count)
    return count


def singleNumber3(A):
    xor = 0
    for i in A:
        xor ^= i
    # return 0

    hashmap = {}
    res = []
    for i in range(0, len(A)):
        temp = xor-A[i]
        if (temp in hashmap):
            res.append(temp)
            res.append(A[i])
        hashmap[A[i]] = i
    
    return res






def goodSubArraysEasy(A, B):
    n = len(A)
    good_sub = 0
    pf = [0]*(n+1)
    # print(pf)
    for i in range(n) :
        pf[i+1] = pf[i] + A[i]
    print(pf)
    for i in range(n) :
        
        for j in range(i, n) :
            print(j+1, i)
            sums = pf[j+1] - pf[i]
            if (j-i+1) % 2 == 0:
                if sums < B :
                    good_sub += 1
            else:
                if sums > B :
                    good_sub += 1
    return good_sub


# A = [1, 2, 3, 4, 5]
# B = 4
# goodSubArraysEasy(A, B)

def forEvenGoodSubArray(sub_list, B, count):
    
    for k in range(len(sub_list)):
        sum = 0
        for l in range(k):
            sum = sum + sub_list[l]
        
        if sum < B and (len(sub_list) % 2 == 0):
            count = count + 1


def forOddGoodSubArray(sub_list, B, count):
    for k in range(len(sub_list)):
        sum = 0
        for l in range(k):
            sum = sum + sub_list[l]
        
        if sum > B and (len(sub_list) % 2 == 0):
            count = count + 1


def maximumPositivity(A):
    maxSizeArray = [0, 0]
    smallestIndex = float("inf")
    checkNonNegativeNumberArray = [0] * len(A)
    flag = 0
    # print(A, checkNonNegativeNumberArray)
    
    for i in range(len(A)):
        if A[i] < 0:
            checkNonNegativeNumberArray[i] = 1
    
    # print(checkNonNegativeNumberArray)

    for j in range(len(A)):
        
        for k in range(j, len(A)):
        
            if (checkNonNegativeNumberArray[j] or checkNonNegativeNumberArray[k]) == 1:
                flag = 1
                break 
        
        
        # print(j, smallestIndex, maxSizeArray[1], maxSizeArray[0], k, j)
        if j < smallestIndex and ((maxSizeArray[1] - maxSizeArray[0]) < (k - j)):
            maxSizeArray[0] = j
            maxSizeArray[1] = k
    
    if flag == 1:
        B = A[maxSizeArray[0]:maxSizeArray[1]]
    else:
        B = A[maxSizeArray[0]:maxSizeArray[1] + 1]
    # print(maxSizeArray)
    # print(B)
    return B


def checkPalindromeRecursion(A):
    l = 0
    r = len(A) - 1
    print(checkPalindromeHelper(A, l, r))


def checkPalindromeHelper(A, l, r):
    if l > r:
        return 1
    if A[l] == A[r]:
        return checkPalindromeHelper(A, l + 1, r - 1)
    return 0


def printStarPattern(A):
    lengthOfRow = 8
    lengthOfColumn = 8

    size = 4
    for i in range(0, size):
        for j in range(i):
            print(" ", end=" ")
        for j in range(size, i, -1):
            print(i, j)
            print()
            print("*", end=" ")
        print()

    # for row in  range(0, (int(lengthOfRow/2))):
    #     for column in range(0, int(lengthOfColumn/2)):
    #         if row <= column:
    #             print("*", end=" ")
    #     print()
    
    # for row in range(int(lengthOfRow/2), 8):
    #     for column in range(int(lengthOfColumn/2), 8):
    #         if row >= column:
    #             print("*", end=" ")
    #     print()

    return 0



def longestPalindromicSubstring(A):
    res = ""
    maxPalindromicValue = 0
    left = 0
    right = 0
    lenOfString = len(A)
    for i in range(0, lenOfString):
        # for Odd Palindrome Finding
        left = i - 1 
        right = i + 1
        print(i)
        while(left >= 0 and right <= lenOfString):
            if A[left] == A[right]:
                left = i - 1
                right = i + 1
            else:
                print(right - left + 1)
                print(maxPalindromicValue)
                print((right - left + 1) > maxPalindromicValue)
                if((right - left + 1) > maxPalindromicValue):
                    maxPalindromicValue = right - left + 1
                    for j in range(left, right):
                        res = res + A[j]
    print(res)
    return 0



def subArrayWithZero(A):
    pSum = [0 for i in range(0, len(A))]

    for j in range(0, len(A)):
        pSum[j] = pSum[j - 1] + A[j]
    
    print(pSum)
    makingHash = {}

    for j in range(0, len(pSum)):
        if pSum[j] not in makingHash:
            makingHash[pSum[j]] = 0
        else:
            makingHash[pSum[j]] += 1
    

    # print(makingHash)

    for k in makingHash:
        if k > 0:
            print(False)
        else:
            print(True)



def kOccurrance(N, B, C):
    demoHash = {}
    sum = 0
    for i in range(0, len(C)):
        if C[i] not in demoHash:
            demoHash[C[i]] = 1
        else:
            demoHash[C[i]] += 1
    
    # print(demoHash)

    for j in demoHash:
        if demoHash[j] == B:
            sum = sum + j

    return sum    


print(1 | 2 | 3)











# A = "abbbbba"
# longestPalindromicSubstring(A)

# print(5 ^ 15)