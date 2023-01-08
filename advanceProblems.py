from itertools import count
import math

def maxCOntinousSubArray(A):
    lengthOfArray = len(A)
    sumOfAllSubArray = []
    maxSum = float('-inf')
    for i in range(0, lengthOfArray):
        sum = 0
        for j in range(i, lengthOfArray):
            sum = sum + A[j]
            sumOfAllSubArray.append(sum)
    
    for k in sumOfAllSubArray:
        maxSum = max(k, maxSum)
    
    return maxSum



def maxContinousSubArrayUsingKadanesAlgo(A):
    # Handle edge case of all array values is negative
    maxSum = float('-inf')

    for i in range(0, len(A)):
        maxSum = max(maxSum, A[i])
    
    
    for j in range(0, len(A)):
        current_sum = current_sum + A[j]
        maxSum = max(maxSum, current_sum)

        if current_sum < 0:
            current_sum = 0

    print(maxSum)
    return 0



# A = [1, 2, 3, 4, -10] 
# A = [-1, -2, -3, -4, -10]
# maxCOntinousSubArray(A)

# A = [ -120, -202, -293, -60, -261, -67, 10, 82, -334, -393, -428, -182, -138, -167, -465, -347, -39, -51, -61, -491, -216, -36, -281, -361, -271, -368, -122, -114, -53, -488, -327, -182, -221, -381, -431, -161, -59, -494, -406, -298, -268, -425, -88, -320, -371, -5, 36, 89, -194, -140, -278, -65, -38, -144, -407, -235, -426, -219, 62, -299, 1, -454, -247, -146, 24, 2, -59, -389, -77, -19, -311, 18, -442, -186, -334, 41, -84, 21, -100, 65, -491, 94, -346, -412, -371, 89, -56, -365, -249, -454, -226, -473, 91, -412, -30, -248, -36, -95, -395, -74, -432, 47, -259, -474, -409, -429, -215, -102, -63, 80, 65, 63, -452, -462, -449, 87, -319, -156, -82, 30, -102, 68, -472, -463, -212, -267, -302, -471, -245, -165, 43, -288, -379, -243, 35, -288, 62, 23, -444, -91, -24, -110, -28, -305, -81, -169, -348, -184, 79, -262, 13, -459, -345, 70, -24, -343, -308, -123, -310, -239, 83, -127, -482, -179, -11, -60, 35, -107, -389, -427, -210, -238, -184, 90, -211, -250, -147, -272, 43, -99, 87, -267, -270, -432, -272, -26, -327, -409, -353, -475, -210, -14, -145, -164, -300, -327, -138, -408, -421, -26, -375, -263, 7, -201, -22, -402, -241, 67, -334, -452, -367, -284, -95, -122, -444, -456, -152, 25, 21, 61, -320, -87, 98, 16, -124, -299, -415, -273, -200, -146, -437, -457, 75, 84, -233, -54, -292, -319, -99, -28, -97, -435, -479, -255, -234, -447, -157, 82, -450, 86, -478, -58, 9, -500, -87, 29, -286, -378, -466, 88, -366, -425, -38, -134, -184, 32, -13, -263, -371, -246, 33, -41, -192, -14, -311, -478, -374, -186, -353, -334, -265, -169, -418, 63, 77, 77, -197, -211, -276, -190, -68, -184, -185, -235, -31, -465, -297, -277, -456, -181, -219, -329, 40, -341, -476, 28, -313, -78, -165, -310, -496, -450, -318, -483, -22, -84, 83, -185, -140, -62, -114, -141, -189, -395, -63, -359, 26, -318, 86, -449, -419, -2, 81, -326, -339, -56, -123, 10, -463, 41, -458, -409, -314, -125, -495, -256, -388, 75, 40, -37, -449, -485, -487, -376, -262, 57, -321, -364, -246, -330, -36, -473, -482, -94, -63, -414, -159, -200, -13, -405, -268, -455, -293, -298, -416, -222, -207, -473, -377, -167, 56, -488, -447, -206, -215, -176, 76, -304, -163, -28, -210, -18, -484, 45, 10, 79, -441, -197, -16, -145, -422, -124, 79, -464, -60, -214, -457, -400, -36, 47, 8, -151, -489, -327, 85, -297, -395, -258, -31, -56, -500, -61, -18, -474, -426, -162, -79, 25, -361, -88, -241, -225, -367, -440, -200, 38, -248, -429, -284, -23, 19, -220, -105, -81, -269, -488, -204, -28, -138, 39, -389, 40, -263, -297, -400, -158, -310, -270, -107, -336, -164, 36, 11, -192, -359, -136, -230, -410, -66, 67, -396, -146, -158, -264, -13, -15, -425, 58, -25, -241, 85, -82, -49, -150, -37, -493, -284, -107, 93, -183, -60, -261, -310, -380 ]
# maxContinousSubArrayUsingKadanesAlgo(A)

def maximumAbsoluteDifference(A):
    maxValue = float('-inf')
    if len(A) == 1:
        return A[0]

    for i in range(1, len(A)):
        for j in range(0, len(A)):
            value = 0
            value = abs(A[i] - A[j]) + abs(i - j)
            maxValue = max(maxValue, value)
        
    print(maxValue)   
    return maxValue


# A = [1, 3, -1]
# A = [2]
# maximumAbsoluteDifference(A)

def maximumAbsoluteDifferenceOptimized(A):
    result = 0
    
    max1 = float('-inf')
    min1 = float('inf')

    max2 = float('-inf')
    min2 = float('inf')

    for i in range(0, len(A)):
        # i = i + 1
        max1 = max(max1, A[i] + i)
        min1 = min(min1, A[i] + i)
        max2 = max(max2, A[i] - i)
        min2 = min(min2, A[i] - i)

    cand1 = abs(max1 - min1)
    cand2 = abs(max2 - min2)

    result = max(cand1, cand2)
    
    return result



# A = [1, 3, -1]
# A = [2]
# maximumAbsoluteDifferenceOptimized(A)


def rainWaterTrapped(A):
    sumOfAllUnitsStored = 0

    for i in range(1, (len(A) - 1)):
        leftMax = leftMaxOfArrayList(A, 0, i)
        rightMax = rightMaxOfArrayList(A, i, (len(A) - 1))
        numberOfUnitsOfWater = min(leftMax, rightMax) - A[i]

        if(numberOfUnitsOfWater >= 0):
            sumOfAllUnitsStored = sumOfAllUnitsStored + numberOfUnitsOfWater
        
    return sumOfAllUnitsStored

def leftMaxOfArrayList(A, startingIdx, endingIdx):
    maxValue = 0
    for j in range(startingIdx, (endingIdx + 1)):
        maxValue = max(maxValue, A[j])
    return maxValue

def rightMaxOfArrayList(A, startingIdx, endingIdx):
    maxValue = 0
    for j in range((endingIdx), startingIdx, -1):
        maxValue = max(A[j], maxValue)
    return maxValue








# A = [0, 1, 0, 2]
# A = [ 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1 ]
# A = [1, 2]
A = [ 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1 ]
rainWaterTrapped(A)




def rainWaterTrappedOptimized(A):
    leftMaxOfA = [0]*len(A)
    leftMaxOfA[0] = A[0]
    result = 0
    for i in range(1, len(A)):
        leftMaxOfA[i] = max(leftMaxOfA[i - 1], A[i])

    i = 0

    rightMaxOfA = [0]*len(A)
    rightMaxOfA[len(A) - 1] = A[len(A) - 1]

    for i in range(len(A) - 2, -1, -1):
        rightMaxOfA[i] = max(rightMaxOfA[i+1], A[i])
    
    i = 0

    for i in range(1, len(A) - 1):
        numberOfUnitsStoredForSingle = min(leftMaxOfA[i - 1], rightMaxOfA[i+1]) - A[i]

        if numberOfUnitsStoredForSingle >= 0:
            result = result + numberOfUnitsStoredForSingle
    
    return result


    return 0

# A = [0, 1, 0, 2]
# A = [ 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1 ]
# A = [1, 2]
# A = [ 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1 ]
rainWaterTrappedOptimized(A)



def rightMax(A):
    maxValue = float('-inf')
    lenOfArray = len(A)
    for i in range(3, 3, -1):
    # for i in range(0, len(A)):
        print(i)
        maxValue = max(A[i], maxValue)
    # print(maxValue)


# A = [ 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1 ]
# A = [5,3,4,2,4]
# rightMax(A)


def mergeIntervals(intervals, newIntervals):
    result = []
    m1 = newIntervals[0]
    m2 = newIntervals[1]
    
    for i in range(0, len(intervals)):
        i1 = intervals[i][0]
        i2 = intervals[i][1]
        print(i1, i2, m1, m2)
        if (m1 > i2):
            result.append([i1, i2])
        elif (i1 > m2):
            result.append([m1, m2])
            m1 = i1
            m2 = i2
        else:
            m1 = min(i1, m1)
            m2 = max(i2, m2)
    result.append([m1, m2])
    print(result)
    return 0


# intervals = [[1, 3], [6, 9]]  
# newIntervals = [2, 5]

# intervals = [[1, 3], [6, 9]] 
# newIntervals = [2, 6]
# mergeIntervals(intervals, newIntervals) 


def firstMissingPositive(A):
    value = 0
    n = len(A)
    for i in range(0, len(A)):
        value = max(value, A[i])
    
    if value == 0:
        return 1
    
    for j in range(0, len(A)):
        while (A[j] != (j + 1) and A[j] > 0 and A[j] <(len(A))):
            if (A[j] != A[A[j] - 1]):
                swap(j, (A[j] - 1), A)
            else:
                break

    for k in range(0, len(A)):
        if (A[k] != (k + 1)):
            return((k + 1))
    return n + 1
def swap(x, y, array):
    temp = array[x]
    array[x] = array[y]
    array[y] = temp

class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        n = len(A)
        i = 0
        while i < n :
            if A[i] > 0 and A[i] < n :
                if A[i] != i+1 :
                    j = A[i]-1
                    if A[i] != A[j] :
                        A[i], A[j] = A[j], A[i]
                        i-=1
            i+=1
        for i in range(n) :
            if A[i] != i+1 :
                return i+1
        return n + 1



# A=[-8, -7, -6]
# A = [1, 2, 0]
# A = [3, 4, -1, 1]
# print(firstMissingPositive(A))



def searchInRowWiseAndColumnWiseSortedMatrix(A, B):
    rows = len(A)
    cols = len(A[0])
    i = 0
    j = cols - 1
    ans = 1000000000000
    while (i < rows and j >= 0):
        if (A[i][j] < B):
            i+=1
        if (A[i][j] > B):
            j-=1
        if (A[i][j] == B):
            if ((i+1) *1009 + (j+1) < ans):
                ans = (i+1) *1009 + (j+1)
            j-=1

    if ans == 1000000000000:
        return -1
    return ans


# A = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
# B = 2

# A = [[1, 2],
#      [3, 3]]
# B = 3
# searchInRowWiseAndColumnWiseSortedMatrix(A,B)


def singleNumberFindingWithXOR(A):
    result = 0
    for i in range(0, len(A)):
        result = result ^ A[i]
    # print(result)
    return result


# A = [1, 2, 2, 3, 1]
# A = [1, 2, 2]
# singleNumberFindingWithXOR(A)


def singleNumberFinding2(A):
    result = [0]*32
    finalResult = 0
    for i in range(0, len(result)):
        for j in range(0, len(A)):
            if((A[j]>>i)&1):
                result[i] = result[i] + 1
    
    for k in range(0, len(result)):
        # print(k)
        if result[k] % 3 == 0:
            result[k] = 0
        else:
            result[k] = 1

    for l in range(0, len(result)):
        if result[l] == 1:
            finalResult = finalResult + (1 * pow(2, l))
    print(finalResult)

def checkBit(n, i):
    return ((n >> i) & 1 == 1)



# A = [0, 0, 0, 1]
# # A = [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
# singleNumberFinding2(A)





# print(gcd(2, 4))


def deleteOneGCD(A):
    leftPrefixGCD = [0]*len(A)
    leftPrefixGCD[0] = A[0]
    
    for i in range(1, len(A)):
        leftPrefixGCD[i] = gcd(leftPrefixGCD[i-1], A[i])

    rightPrefixGCD = [0]*len(A)
    rightPrefixGCD[len(A) - 1] = A[len(A) - 1]

    for j in range(len(A) - 2, -1, -1):
        rightPrefixGCD[j] = gcd(rightPrefixGCD[j + 1], A[j])
    
    leftMaxGCD = 0
    rightMaxGCD = 0
    result = 0
    for k in range(0, len(A)):
        if k == 0:
            leftMaxGCD = 0
            rightMaxGCD = rightPrefixGCD[k + 1]
        elif k == len(A) - 1:
            leftMaxGCD = leftPrefixGCD[k - 1]
            rightMaxGCD = 0
        else:
            leftMaxGCD = leftPrefixGCD[k - 1]
            rightMaxGCD = rightPrefixGCD[k + 1]
        
        result = max(gcd(leftMaxGCD, rightMaxGCD), result)
    return 0


def gcd(a, b):
    if  b == 0:
        return a
    return gcd(b, a%b)


# A = [5, 15, 30]
# deleteOneGCD(A)

def pubg(A):
    result = 0
    for i in range(0, len(A)):
        result = gcd(result, A[i])
    return result

# A = [6, 4]
# A = [2, 3, 4]
# pubg(A)

def maxArr(A):
    maxValue = float('-inf')
    if len(A) == 1:
        return A[0]

    for i in range(1, len(A)):
        for j in range(0, len(A)):
            print(i, j)
            value = 0
            value = abs(A[i] - A[j]) + abs(i - j)
            maxValue = max(maxValue, value)
        
    print(maxValue)   
    return maxValue

# A = [1, 3, -1]
# maxArr(A)


def plusOne(A):
    if A[0] == 0:
        A.pop(0) 
    A[len(A) - 1] = A[len(A) - 1] + 1
    print(A)
    return A


def beggarProblem(A, B):
    beggers = [0]*A
    hash = {}
    for i in range(0, len(B)):
        if B[i][2] not in hash:
            hash[B[i][2]] = [B[i][0] - 1, B[i][1]]
        else:
            print(hash[B[i][2]])
            # hash[B[i][2]] = hash[B[i][2]].append([B[i][0] - 1, B[i][1]])
    i = 0
    for i in hash:
        for j in range(hash[i][0], hash[i][1]):
            beggers[j] = beggers[j] + i        
    # print(beggers)
    return beggers

    

# A = 5
# B = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
# A = 5
# B = [
#   [1, 2, 100],
#   [2, 5, 100],
#   [3, 4, 100]
# ]
# beggarProblem(A, B)

# hash = {100: [2,4]}
# a = 100
# if a in hash:
#     print('true')
# else:
#     print('false')


def mergrRect(a, b, c, d, e, f, g, h):
    if c < e and d < f:
        return 1
    elif a < g and b < h:
        return 1
    else:
        return 0


# if F>=D or B>=H or E>=C or A>=G:

# A = 0
# B = 0
# C = 4
# D = 4
# E = 2
# F = 2
# G = 6
# H = 6

# A = 0
# B = 0
# C = 4
# D = 4
# E = 2
# F = 2
# G = 3
# H = 3

# A = 1
# B = 1
# C = 4
# D = 4
# E = 0
# F = 0
# G = 2
# H = 2


def addOneToNumber(A):
    i = 0
    resultArray = []
    if len(A) == 1 and A[0] == 0:
        return resultArray.append(A[0] + 1)
    while i < len(A): 
        if A[i] == 0:
            A.pop(0)
        else:
            break
        i = i + 1 
    i = 0
    carry = 0
    plusOneAddition = 1
    for i in range(len(A) -1, -1, -1):
        digit = 0
        addition = 0
        if plusOneAddition == 1:
            addition = A[i] + plusOneAddition
            plusOneAddition = 0
        elif plusOneAddition == 0 and carry == 0:
            addition = A[i]
        elif carry > 0:   
           addition = carry + A[i]
           carry = 0
        digit = int(addition%10)
        carry = int(addition/10)
        resultArray.append(digit)
    if carry > 0:
        resultArray.append(carry)
    carry = 0
    return list(reversed(resultArray))




# A = [0,0,1, 0, 0]
# A = [9, 9, 9]
# A = [1, 2, 3]
# A = [0]
# addOneToNumber(A)


def maxNonNegativeSubArrayWithIndices(A):
    max_value = [0, 0, 0]
    result = []
    for i in range(0, len(A)):
        if A[i] > max_value[0]:
            max_value[0] = A[i]
            max_value[1] = i
            max_value[2] = i + 1
    
    current_sum = [A[0], 0, 1]
    i = 0

    for i in range(1, len(A)):
        if current_sum[0] >= 0:
            current_sum[0] = current_sum[0] + A[i]
            current_sum[1] = current_sum[1]
            current_sum[2] = i + 1

            if current_sum[0] > max_value[0]:
                max_value[0] = current_sum[0]
                max_value[1] = current_sum[1]
                max_value[2] = current_sum[2]
        else:
            current_sum[0] = 0
            current_sum[1] = i -1 
            current_sum[2] = i
    
    i = 0

    if max_value[0] == 0:
        return [0, 0]
    
    for i in range(max_value[1], max_value[2]):
        result.append(A[i])
    
    return result
    

# A = [1, 2, 5, -7, 2, 3]
# A = [10, -1, 2, 3, -4, 100]
# A = [1,2,4,-8,1,2,4, 4]
# A = [ 0, 0, -1, 0 ]
# maxNonNegativeSubArrayWithIndices(A)


def solve(A):
    N = len(A)

    def createspf(n):
        spf = [i for i in range(n)]
        rng = math.sqrt(len(spf))
        i = 2
        while i < rng:
            if spf[i] == i:
                j = i * i
                while j < n:
                    if spf[j] == j:
                        spf[j] = i
                    j += i
            i += 1
        return spf
        
    def primefactors(spf,n):
        total = 1
        print(spf[n])
        while n > 1:
            prime = spf[n]
            count = 0
            print("first while loop",  n)
            while n % prime == 0:
                if spf[n] == 2:
                    print(n)
                count += 1
                n = n // prime
            total = total * (count +1)
        print("hello", total)
        return total

        
    spf = createspf(max(A)+1)
    res = []
    print(spf)
    for k in range(N):
        print(A[k])
        value = primefactors(spf,A[k])
        res.append(value)
        
    return res

# A = [1,2,3,4,72]
# solve(A)


def distinctPrimes(A):
    
    distinctPrimes = []

    for i in range(0, len(A)):

        if i % g != 0:
            distinctPrimes.append(i)

    
    return distinctPrimes


# A = [1, 2, 3, 4]
# print(math.sqrt(24))
# distinctPrimes(A)


def power(A, B, C):
    
    if B == 0:
        return 0
    
    if B == 1:
        return A
    
    return (power(A, B - 1, C) * power(A, 1, C)) % C
     

# A = 2 
# B = 3
# C = 3
# print(power(A, B, C))


# print(-1%20)


'''
Observations:
- What they want us to do is flip the input which will be of 0's and 1's eg. 1000001111, after fliping 1111111111
- We need to give as output where the most contigous 1's are present eg. for this 1000001111 after flipping 0111110000 the o/p is (2, 6)
- we can also do the following of not flipping the numbers 
- the Output should be lexicographically smallest one eg. for 010 -> o/ps can be  
- You can only do one operations
Algo
- Using Kadane's Algo
    1. We make a new araay flipping 0 -> 1 and 1 -> -1 after
    2. Will need to make a a new array of 3 length that will store the sum, start range and end range 
    3. I iterate through that array and find the max sum with the start range and end range
    4. the final result will be compared with the sum and also the start range where current_sum > sum && start_range > current_start_range 

Edge Cases To Handle:
1. We will need to return with no array if all the array element is 1 and handle this at first only
2. if 1's are more than 0's then we need to first store the array value of the sum with start range and end range

'''



def flip(A):
    # A = 1000001111
    countOfOnes = 0
    countOfZeros = 0
    for i in range(0, len(A)):
        if A[i] == 1:
            countOfOnes = countOfOnes + 1
        if A[i] == 0:
            countOfZeros = countOfZeros + 1
                
    '''
    A = 1000001111
    countOfZeros = 5
    countOfOnes = 5
    '''
    if len(A) == countOfOnes:
        return []

    prefixSum = []
    i = 0




    for i in range(0, len(A)):
        if A[i] == 0:
            prefixSum.append(1)
        else: 
            prefixSum.append(-1)
    
    '''
    A = 1000001111
    prefixSum = [-1, 1,1,1,1,1,-1,-1,-1,-1]
    '''
    print(prefixSum)
    max_sum = [0, float('inf'), float('inf')]

    current_sum = [prefixSum[0], 0 , 1]

    i = 0

    for i in range(1, len(prefixSum)):
        if current_sum[0] > 0:
            current_sum[0] = current_sum[0] + prefixSum[i]
            current_sum[1] = current_sum[1]
            current_sum[2] = current_sum[i + 1]

            if current_sum[0] > max_sum[0] and current_sum[1] < max_sum[1]:
                max_sum[0] = current_sum[0]
                max_sum[1] = current_sum[1]
                max_sum[2] = current_sum[2]


        else:
            print("esk s")
            current_sum[0]= 0
            current_sum[1]= i - 1
            current_sum[2]= i
    
    print(max_sum[1], max_sum[2])
    return [max_sum[1], max_sum[2]]

'''
Observations


'''



def mergeTwoArrays(A, B):
    result = [0] * (len(A) + len(B))
    p1 = 0
    p2 = 0
    p3 = 0
    while(p1 < len(A) and p2 < len(B)):
        if A[p1] <= B[p2]:
            result[p3] = A[p1]
            p1 = p1 + 1
            p3 = p3 + 1
        else:
            result[p3] = B[p2]
            p2 = p2 + 1
            p3 = p3 + 1

    while(p1 < len(A)):
        result[p3] = A[p1]
        p1 = p1 + 1
        p3 = p3 + 1

    while(p2 < len(B)):
        result[p3] = B[p2]
        p2 = p2 + 1
        p3 = p3 + 1            
    
    return result




# A = [4, 7, 9 ]
# B = [2, 11, 19 ]

# A = [1]
# B = [2]
# [2, 4, 7, 9, 11, 19]

# mergeTwoArrays(A, B)

def swap(A, i , j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp



def kThSmallestElement(A, B):
    for i in range(0, B):
    
        toBeSwapped = [A[i], i]
        minValue = [float('inf'), -1]

        for j in range(i+1, len(A)):
            if A[j] < minValue[0]:
                minValue[0] = A[j]
                minValue[1] = j
        if toBeSwapped[0] > minValue[0]:
            A[toBeSwapped[1]], A[minValue[1]] = A[minValue[1]], A[toBeSwapped[1]]
    print(A)
    return A[B - 1]    

# A = [2, 1, 4, 3, 2]
# B = 3

# A = [1, 2]
# B = 2

# A = [ 8, 16, 80, 55, 32, 8, 38, 40, 65, 18, 15, 45, 50, 38, 54, 52, 23, 74, 81, 42, 28, 16, 66, 35, 91, 36, 44, 9, 85, 58, 59, 49, 75, 20, 87, 60, 17, 11, 39, 62, 20, 17, 46, 26, 81, 92 ]
# B = 9
# kThSmallestElement(A, B)



def longestConsecutiveSequece(A):
    hashSet = set(A)
    result = 1

    for value in hashSet:
        print("skns")
        print(value)
    return 0

A = [100, 4, 200, 1, 3, 2]
# A = [2, 1]
longestConsecutiveSequece(A)



















