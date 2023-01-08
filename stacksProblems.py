def nearestSmallestElement(A):
    resultArray = [0]*len(A)
    stack = []
    resultArray[0] = -1
    stack.append(A[0])
    
    for i in range(1,len(A)):
        if len(stack) == 0:
            resultArray[i] = -1
            stack.append(A[i])
        else:
            while(len(stack) != 0):
                currentTopElementOfStack = stack[-1]
                if A[i] > currentTopElementOfStack:
                    resultArray[i] = currentTopElementOfStack
                    stack.append(A[i])
                    break
                else:
                    stack.pop()
            resultArray[i] = -1
            stack.append(A[i])


    return resultArray

A = [4, 5, 2, 10, 8]
# A = [3, 2, 1]
print(nearestSmallestElement(A))