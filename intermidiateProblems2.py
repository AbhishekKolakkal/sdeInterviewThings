
def longestCommonPrefix(A):


    resultstring = ''
    minlen = 1000000

    for each in A:
        if(minlen>len(each)):
            minlen = len(each)
    
    i = 0
    while(i<minlen):
        for j in range(1,len(A)):
            if(A[j][i]!= A[j-1][i]):
                return resultstring
        resultstring+=A[0][i]
        i+=1
    return resultstring    

# A = ["abcdefgh", "aefghijk", "abcefgh"]
# # A = ["abab", "ab", "abcd"]
# longestCommonPrefix(A)



# def shaggyAndDistance(A):
#     '''
#     Problem Statement says that i need to find the minimum disctance of a possible array path
#     Sorting is not possible as it canmake the values and position ambigoius
#     we want to find a special pair such that the distance between the pair is minimum
#     It can only be i - j not j - i 
#     if no special pair then return -1

#     Doodles
#     in the brute force method i can do this is 2 loops where first pair is to find the number and second pair is to find the other position of the number and check for minimum value and return it

#     SOrting cannot be applied

#     hashing method where I use hashmap to store the number and the distance
#     eg: {
#         7: [0, 5, 6],
#         1: [1, 4],
#         3: [],
#         4: []
#     }    

#     this application wont work when we have more than 2 same numbers
#     actually this will work what I only need to do that iterate and check with the previous number

#     Algo
#     1. Making of the hash
#         a. if the number is not present then put in the hash in this format 7: [0]
#         b. if the number is already present then append the number again
#     2. initiate a result variable with max number
#     3. iterate through the hash 
#         a. you will get the value as array 
#         b. once I get the array 2 possibilities, 
#             1. if the array is empty then skip
#             2. if the array is not empty then need to do some computation
#                 a. start the iteration with 1 index,  check and do subtraction with the previous index and move on
#     4. the minimum value needs to be checked if it is changed or not
#         a. if it is changed then return the result 
#         b. if not then get the return -1
#     '''
#     result = -1
#     if len(A) == 0 or len(A) == 1:
#         return result
    
#     minimumValue = float('inf')
    
#     #making of the hash
    
#     hashmapWithDistance = {}

#     for i in range(0, len(A)):
#         if A[i] not in hashmapWithDistance:
#             hashmapWithDistance[A[i]] = [i]
#         else:
#             hashmapWithDistance[A[i]].append(i)
    

#     i = 0

#     for _, value in hashmapWithDistance.items():
#         if len(value) > 1:
#             for j in range(1, len(value)):
#                 minimumValue = min(minimumValue, value[j] - value[j - 1])
    

#     if minimumValue == float('inf'):
#         return -1
#     else:
#         return minimumValue



def shaggyAndDistance(A):
    mydict = {}
    ans = 1000000000
    c = 0
    for i in A:
        # checks if A[i] has occurred previously
        if i in mydict:
            ans = min(ans, c - mydict[i])
            mydict[i] = c
        else:
            mydict[i] = c
        c = c + 1
    if ans == 1000000000:
        ans = -1
    print(mydict)
    return ans




def subarrayWithGivenSum(A, B):
    '''
    The problem statement states that I will be getting only +ve numbers of array and I need to return first continous subaaray which adds to the sum given
    if no answer return -1
    it can only have minimum subarray means we can only have continous array

    Doodles
    The brute force approach will be to consider all subarray and find the pair which gives the sum but this will only give me subaary sum not the one as which is the first TC: O(n3) SC O(1)

    I can use sliding window technique where I first take 1 element, if the sum is smaller then increase the window size till it reaches the sum if in somehow it reaches that the sum is greater than the sum move to next element. But for this the array should be in sorted manner TC: O(nlogn) SC O(1)

    To get the subArray only I will have n2 complexity that means I need to do some mor things  

    can I use prefix over here ?
    [1, 2, 3, 4, 5]
    [1, 3, 6, 10, 15]
    6 - 1 = 5
    1 position and 0 position 

    [5, 10, 20, 100, 105]
    [5, 15, 35, 135, 240]

    B = 120
    5-5 = 0
    15 - 5 = 10
    35 - 5 = 30
    135 - 5 = 130
    reset i and j to 
    35 - 15 = 20
    135 - 15 = 120

    Algo 
    1. Need to find the prefix sum of the array
    2. We will need to initialzie a variable for this which will have the value as [0, 0]
    2. Once I find the prefix sum I will be using a while loop which will have () as condition
        a. Now in the while loop i will start from 0 and j will also start from 0
            1. We will need a check that if the final sum is greater than the difference then increament j
            2. if the difference is greater than sum then reset i and j to i++ and i = j
            3. if I get the value then return with the value
    3. Check if you got the value by checking if first initialize variable is the same
        a. If it is same then return -1
        b. if the value is not same return the value array
    '''

    if len(A) == 0:
        return -1

    if len(A) == 1 and B == A[0]:
        return [0, 0]

    result = [0, 0]

    # Find prefix sum
    prefixSumArr = [0 for i in range(0, len(A))]
    prefixSumArr[0] = A[0]
    for i in range(1, len(A)):
        prefixSumArr[i] = prefixSumArr[i - 1] + A[i]


    i = 0
    j = 1

    while (i < len(A) and j < len(A)):
        diff = prefixSumArr[j] - prefixSumArr[i]
        if diff < B:
            j = j + 1
        elif diff > B:
            i = i + 1
            j = i + 1
        else:
            result = A[i + 1:j+1]
            break

    print(result)
    if result == [0, 0]:
        return -1
    else:
        return result

# A = [1, 2, 3, 4, 5]
# B = 5
# A = [5, 10, 20, 100, 105]
# B = 110
# A = [ 23, 50, 44, 6, 39, 15, 44, 27, 47, 29, 30, 44, 28, 42, 7, 32, 16, 40, 8, 7, 5, 48, 48, 16, 9, 5, 50, 16, 18, 9, 21, 26, 48, 37, 27, 7, 5, 29, 24, 28, 10, 44, 21, 1, 48, 15, 31, 41, 42, 23, 4, 32, 40, 40, 27, 20, 29, 42, 25, 18, 37, 43, 13, 30, 42, 24, 17, 42, 14, 42, 43, 36, 31, 29, 24, 24, 8, 3, 12, 34, 14, 6 ]
# B = 62
# subarrayWithGivenSum(A,B)


def magicNumber(A):
    '''
    magic numbers means add till you get 1 if not then not a magic number
    we need to return 1 if the number is magic and 0 if the number is not magic
    Here we need to not that the addition is only done till you reach single digit number till then I need to do the addition

    doodle
    the number i have is 83557
    now if I divide 83557//10 then i will get 8355 
    if i mode then 83557%10 then i will get 7 
    I will need to repeat this procuedure till I get , till the division gives me 0 i.e 
    83557//10 = 8355


    '''
    if A == 1:
        return 1
    if A< 10:
        return 0
    
    sum = 0
    while (A > 0):
        last_digit = A%10
        A = A//10
        sum = sum + last_digit 
    return magicNumber(sum)

# # A = 83557
# A = 1291
# print(magicNumber(A))



def distinctWindowNumbers(A, B):
    '''
    we need to return the count of distinct number in the window size of the array
    the function will return an array
    if B > N return empty array

    [1, 2, 1, 3, 4, 3] and window size is 3
    [1,2,1] = 2
    [2,1,3] = 3
    [1,3,4] = 3
    [3,4,3] = 2

    algo
    1. first check if B > N then return []
    2. initialize result with empty array
    3. we will be doing a for loop starting with 0 to len(A) - 3
        a. in this for loop we will be slicing the array in +2
        b. put the value in set and get the count and append in the result array
        c. Once done move on
    '''

    result = []

    if B > len(A):
        return result
    
    for i in range(0, len(A) - B + 1):
        hashset = set()
        count = i
        while (count < i + B):
            hashset.add(A[count])
            count += 1
        result.append(len(hashset))
    return result



# A = [1, 2, 1, 3, 4, 3]
# B = 3
# A = [1, 1, 2, 2]
# B = 1
# distinctWindowNumbers(A, B)


def kthSymbol(A, B, firstValue):
    result = ""
    for i in range(0, len(firstValue)):
        if firstValue[i] == "0":
            result.join("01")
        if firstValue[i] == "1":
            result.join("10")
    print(result)



A = 1
B = 1

# A = 2
# B = 2
kthSymbol(A, B, "0")