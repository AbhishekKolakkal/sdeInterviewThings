
def singleNumber3(A):
    '''
    Approach:
    1. do ^ operation on the array and get the answer
    2. Once you get the answer we need to check which bit is set, now to check which bit is set 
        1. use a checkbit operation and return if you get the first check bit 
    3. once i get the value, i will need to make 2 arrays 
        1. Where if the bit is set then it is in one group else it is in another group
    4. after this Xor both the array group
    5. return the answer in sorted manner
    '''

    
    result = []

    xorResultOfArr = 0

    if len(A) == 2:
        return sorted(A)

    
    for i in range(0, len(A)):
        xorResultOfArr = xorResultOfArr ^ A[i]

    i = 0
    firstSetNumberOfAnswer = []

    for i in range(0, 32):
        if xorResultOfArr & (1 << i):
            firstSetNumberOfAnswer.append(i)


    setBitArr = []
    unsetBittArr = []

    i = 0

    for i in range(0, len(A)):
        if A[i] & (1 << firstSetNumberOfAnswer[0]):
            setBitArr.append(A[i])
        else:
            unsetBittArr.append(A[i])
    

    i = 0
    xorResultOfArr = 0
    for i in range(0, len(setBitArr)):
        xorResultOfArr = xorResultOfArr ^ setBitArr[i]
    
    result.append(xorResultOfArr)

    i = 0
    xorResultOfArr = 0

    for i in range(0, len(unsetBittArr)):
        xorResultOfArr = xorResultOfArr ^ unsetBittArr[i]
    
    result.append(xorResultOfArr)

    return sorted(A)    

# A = [1, 2, 5, 1, 2, 4]
# A = [1, 2]
# print(singleNumber3(A))

def interestingArray(A):
    '''
    Approach:
    1. We know that an even number can be split into 2 same digit and Xoring them will give a 0 so we can just add or pop the value
    2. we can xor the rest array and check for if the digit can be zor again if not then return the value like that only
    '''
    value = 0
    for i in range(0, len(A)):
        if A[i]%2 == 0:
            A[i] = 0
        
    i = 0
    for i in range(0, len(A)):
        value^=A[i]
    
    if value%2 == 0:
        print("Yes")
        return "Yes"
    else:
        print("No")
        return "No"
    
    return 0



# A = [9, 17]
# A = [1]
# interestingArray(A)

def repeatedNumber(A):
    '''
    actual_sum = array_sum +  A - B
    actual_sum - array_sum = A - B
    '''
    a = 0
    b = 0

    array_sum = 0
    for i in range(0,len(A)):
        array_sum += i
    
    actual_sum = 0
    i = 0

    for i in range(0, len(A)):
        actual_sum += A[i]
    
    i = 0
    for i in range(0, len(A)):
        a &= A[i]
    
    b = actual_sum - array_sum - A

    return 0

A = [3, 1, 2, 5, 3]
# A = [1 2 3 4 5]

'''
15 - 14 = 3 - B

1 = 3 - B
'''

# repeatedNumber(A)

def sumOfPairwiseHammingDistance(A):
    '''
    0010 -> setBit = 1 and unsetBit = 3
    0100 -> setBit = 1 and unsetBit = 3
    0110 -> setBit = 2 and unsetBit = 2

    01010 3 
    01101 2
    01111 1

    2
    3
    4

    '''
    return 0


# A=[2, 4, 6]
# A=[10,13,15]
# sumOfPairwiseHammingDistance(A)

def smallestXor(A, B):
    '''
    eg A = 3, B = 3 here there should be a X that I can XOR with A but the answer should be as minimum as possible and set bit should be equal to B
    01111
    01100
    00011

    Approach:
    1. If B is 0 then return the same answer again
    2. I will have a bin variable which will have value as 32
    3. Will also need 
    4. I will do a for loop on the number A and check for set bit from the left as I need the MSB coz I need the minimum answer
        1. If i get a set bit then unset the bit and store the value in variable x and decreament the B by 1 and do this till i get B is 1
    5. Return the X

    '''
    if B == 0:
        return A
    x = A
    for i in range(31, -1, -1):
        if ((x >> i) & 1) == 1:
            B -=1
            if B < 0:
                x = x & (~(1 << i)) 

    print(x)    
    return 0


# A = 3
# B = 3

# A = 15
# B = 2
# smallestXor(A, B)


def maximimSatisfaction(A):
    '''
    Approach:
    1. I will have an array with 32 0's in it
    2. I will have a for which will go from 31 to 0 in reverse 
        1. In that for loop another loop that will check the array and if we have a set bit, 
            - if a set bit is there then increase the count by 1 for every array values
    3. lastly it will check which has 4 value as count return it
    '''
    result = ''

    countArr = [0] * 32
    
    for i in range(31, -1, -1):
        count = 0
        for j in range(0, len(A)):
            if ((A[j] >> i) & 1) == 1:
                count = count + 1

        countArr[i] = count 

    i = 0

    for i in range(len(A) -1, -1, -1):
        if A[i] != 4:
            result = "".join([result, "0"])
        else:
            result = "".join([result, "1"])
    
    result = "".join(reversed(result))
    print(int(result))
    
    return 0

A = [10, 20, 15, 4, 14]
# A = [2, 2, 7, 15]
maximimSatisfaction(A)



'''
001111 -> 15
001110 -> 14
010100 -> 20
000100 -> 4
001010 -> 10


00010 -> 2
00010 -> 2
00111 -> 7
01111 -> 15

00001
00010
00100
01000
10000
'''

















