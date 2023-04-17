
def fibonacci2(A):
    '''
    you have given f0 = 0, f1 = 1
    f2 = f0 + f1
    f3 = f0 + f1 + f2
    f4 = f0 + f1 + f2 + f3
    Fn = Fn-1 + Fn-2
    F4 = F4-1 + F4-2 -> F3 + F2


    Approach
    Assumption: The function should return fibonici
    Main Logic: return fibonacci(n - 1) + fibonacci(n - 2)
    base Condiction: will be that it should stop at f0 giving the answer of f0 or f1 also 
    '''
    if A == 0:
        return 0
    
    if A == 1:
        return 1
    
    return fibonacci2(A - 1) + fibonacci2(A - 2)



# A = 2
# A = 9
# print(fibonacci2(A))

def sumOfDigitsHelper(A, res):

    
    mod = A%10
    A = A//10
    res = res + mod
    if A == 0:
        return res
    return sumOfDigitsHelper(A, res)

def sumOfDigits(A):
    '''
    46//10 -> 4
    46%10 -> 6
    Now I need 6 and add that 6 to then result number and pass the divided number again

    Approach:
    Assumpotion: The function should return Number
    Main Logic: mod = num%10
                num = num//10
                result = result + mod
                
    Base Condition : If I come accross 0 then return the result then and there only 
    '''
    
    result = 0
    return sumOfDigitsHelper(A, result)



# A = 46
# A = 11
# print(sumOfDigits(A))


def factorial(A):
    '''
    the factorial of 4 will be 
    F(4) = 4 * 3 * 2 * 1
    F(4) = 4 * F(3)
    and to find F(3)
    F(3) = 3 * F(2)

    Approach:
    Assumption: We need a funtion that returns Factorial(n)
    Main Logic: return A * F(A - 1)
    Base Case: when it reaches to 1 then we would be returning F(1) as 1
    '''
    if A == 1:
        return 1
    
    return A + factorial(A - 1) + 1


# A = 3
# A = 1
# print(factorial(A))

def kthSymbol(A, B):
    '''
    r1: 0
    r2: 01
    r3: 0110
    r4: 01101001
    r5: 0110100110010110

    the output get doubled in 2^n times always 
    it is given that 0 on the next can be 01 and 1 can be 10
    the first part is repeating and the second part is complement of it

    now to find r5 we will need r4 will need r3 will need r2 will need r1

    Assumption: our fucntion will return a string with 01 made in it
    Main Logic: it will take previous data and concate the compliment of it
    Base Case: if A is 1 then return 0
    '''

    if A == 1:
        return '0'

    return 0



A = 2
B = 1
A = 2
B = 2
kthSymbol(A, B)
