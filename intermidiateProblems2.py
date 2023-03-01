
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
    print(resultstring)
    return resultstring    

A = ["abcdefgh", "aefghijk", "abcefgh"]
# A = ["abab", "ab", "abcd"]
longestCommonPrefix(A)