def beggarsProblem(A, B):
    '''
    It is given that there are A beggers sitting in a row which means we have 5 beggars for the input given
    so you have another 2 d Array given which has 3 values in it
    0th -> Left range 1th -> Right range 2nd Value -> the amout donated
    I want to give amounts like the total amount received by the beggar at the end of the day
    [0,0,0,0,0] 
    when I took first array it did this
    [10, 10, 0, 0, 0]
    when i tool second array it did this
    [10, 30, 20, 0, 0]
    when I took 3rd array 
    [10, 55, 45, 25, 25] 
    
    Approach
    1. need to have an array with n length of 0's 
    2. i will be having a for loop for B in which will take the value and add the positive value in the start index and negative value in the end index
        1. here we will need to handle condition for value being there already, if the value is there already then I need to add with the previous value and add the new value

    3. once this is done then I will do a sum 

    '''
    result = [0] * A
    for i in range(0, len(B)):
        numberToAdd = B[i][2]
        result[B[i][0] - 1] = result[B[i][0] - 1] + numberToAdd
        if B[i][1] < A:
            result[B[i][1] - 1 + 1] = result[B[i][1] - 1 + 1] + (-numberToAdd)
    
    # [10, 0, -10, 0, 20]

    i = 0
    for i in range(1, len(result)):
        result[i] = result[i] + result[i - 1]

    return result

# A = 5
# B = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
# beggarsProblem(A, B)


'''
 A = [5, -2, 3 , 1, 2]
 B = 3

 the prefix sum will be
[5, -2, 3 , 1, 2]


prefix[a-1] + suffix[n-(k-a)]

if i pick elements from left one by one means


 A = [ 2, 3, -1, 4, 2, 1 ]
 B = 4

[ 2, 3, -1, 4, 2, 1 ]

prefix = [2, 5, 4, 8, 10, 11]
suffix = [11, 9, 6, 7, 3, 1]
k = 4
prefix[a - 1] + suffix[n - (k - a)]

3 + (6 - (4 - 4))

2 + (6 - (4 - 2))
2 + 4


'''

def pickFromBothSides(A, B):
    '''
    Approach without prefix sum and suffix sum
    1. I will need to have a result which will have the minimum value
    2. Need a for loop where it will go through B len and find the sum
    3. Now I need to have another loop which will be till the B value is > 0
        1. I will subtract the B - 1 and add N - 1
        2. After this will decreament the value of N - 1 -1 and also B - 1 - 1
        3.  

    '''
    result = float('-inf')
    sum = 0
    for i in range(0, B):
        sum += A[i]
    
    N = len(A) - 1
    result = max(result, sum)
    while B > 0:
        sum = sum + A[N] - A[B - 1]
        result = max(result, sum)
        B -=1
        N -=1
    return result


# A = [5, -2, 3 , 1, 2]
# B = 3
# A = [ 2, 3, -1, 4, 2, 1 ]
# B = 4
# pickFromBothSides(A, B)


def flipOnes(A):
    '''
    Approach
    first we will convert 1's to -1
    then use kadane's algo

    '''
    arrOfCOnvertedStringValues = [0] * len(A)
    for i in range(0, len(A)):
        arrOfCOnvertedStringValues[i] = -1 if A[i] == "1" else 1


    # [1, 2, 3, -7, 5, 6, 11]
    i = 0
    sum = 0
    l, r = 0, 0
    currentSum = arrOfCOnvertedStringValues[0]

    for i in range(1, len(arrOfCOnvertedStringValues)):
        currentSum = currentSum + arrOfCOnvertedStringValues[i]
        if currentSum > sum:
            sum = currentSum
            r = i
        
        if currentSum < 0:
            currentSum = 0
            l = i

    print(l, r)
    return 0




A = "010"
# A = "111"
flipOnes(A)


def equilibriumIndexOfAnArray(A):
    '''
    if only 1 element in the array then return as 0
    over in the array i can find the whole sum first
    then make a variable as leftEquilibrium and rightEquilibrium which will have values like this 0, wholeSum 
    now after a for loop I will minus the value and checkt the left and right equilibrium value if it is same then count should be increased
    there is an edge case where I need to handle 
    '''

    if len(A) == 0 or len(A) == 1:
        return 0

    wholeSum = 0
    for i in range(0, len(A)):
        wholeSum += A[i]
    

    i = 0
    minEqIndex = float('inf')
    leftEquilibrium = 0
    rightEquilibrium = wholeSum
    
    # [-7, 1, 5, 2, -4, 3, 0]
    for i in range(0, len(A)):
        if i == 0:
            rightEquilibrium = rightEquilibrium - A[i]
        else:
            rightEquilibrium = rightEquilibrium - A[i]
            leftEquilibrium = leftEquilibrium + A[i - 1]


        if rightEquilibrium == leftEquilibrium:
            return i


    return 0
    




# A = [-7, 1, 5, 2, -4, 3, 0]
# A = [1, 2, 3]
# print(equilibriumIndexOfAnArray(A))





import re
import unicodedata

def parameterize(string_to_clean, sep = '-'):
    parameterized_string = unicodedata.normalize('NFKD', string_to_clean).encode('ASCII', 'ignore').decode()
    print(parameterized_string)
    parameterized_string = re.sub("[^a-zA-Z0-9\-_]+", sep, parameterized_string)
    print(parameterized_string)
    if sep != None and sep != '':
        parameterized_string = re.sub('/#{re_sep}{2,}', sep, parameterized_string)
        parameterized_string = re.sub('^#{re_sep}|#{re_sep}$', sep, parameterized_string, re.I)

    print(parameterized_string)
    return parameterized_string.lower()

string = "Women's Drape Chiffon Party/ Evening/ Gown in Purple"
parameterize(string)










