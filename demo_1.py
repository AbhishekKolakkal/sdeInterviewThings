from distutils.sysconfig import customize_compiler
from lib2to3.pytree import LeafPattern


def commonElements(A, B):
    dictOfFirstArray = {}
    ret = []
    for i in range(len(A)):
        if A[i] not in dictOfFirstArray:
            dictOfFirstArray[A[i]] = 1
        else:
            dictOfFirstArray[A[i]] = dictOfFirstArray[A[i]] + 1

    print(dictOfFirstArray)


    for j in range(len(B)):
        if B[j] in dictOfFirstArray:
            if dictOfFirstArray[B[j]] != 0:
                ret.append(B[j])
                dictOfFirstArray[B[j]] -= 1

    return ret 



def firstRepeatingNumber(A):
    dictOfArray = {}

    for i in range(len(A)):
        if A[i] not in dictOfArray:
            dictOfArray[A[i]] = 1
        else:
            dictOfArray[A[i]] = dictOfArray[A[i]] + 1

    # print(dictOfArray)
    # print(A)
    for j in range(len(A)):
        # print(j)
        if dictOfArray[A[j]] > 1:
            # print(A[j])
            return A[j]
    
    return -1



def largestSumBubArray(A):
    maxSum = A[0]
    lefPtr = 0
    while lefPtr < len(A):
        walkingPtr = lefPtr + 1
        maxSum = max(maxSum, maxSum + A[walkingPtr])
        walkingPtr += 1
        LeftPtr =+ 1
    
    print(maxSum)



def solveEquilibrium(A):
    n = len(A)
    summ = 0
    for i in A:
        summ += i
    l = 0
    # print("szjbsjk", summ)
    for i in range(0, n):
        print(summ, i, A[i])
        # print("sgbhsvs", summ - A[i])
        summ -= A[i]
        print(summ, i, A[i])
        if l == summ :
            return i
        l += A[i]
    return -1







A=[-7, 1, 5, 2, -4, 3, 0]
solveEquilibrium(A)














