# 100
#  11

# 001 = 3
# 11 = 2

# 0 + 1

# 1%2
# 1/2 = 0.5




def addBinary(A, B):
    A = A.strip()
    B = B.strip()
    print(type(A), type(B))
    n = len(A)
    m = len(B)
    print(n, m)
    if n < m:
        print("INSIDE")
        A,B = B,A
        n,m = m, n
    ret = ""
    carry = 0
    A = A[::-1]
    B = B[::-1]
    print(A, B)
    print("sjbdkd", m)
    print("range(m)", range(m))
    print("range(m, n)", range(m,n))
    for i in range(m):
        # print("A",A[i])
        # print("B", B[i])
        tempA = int(A[i])
        tempB = int(B[i])
        tempRet = (tempA + tempB + carry)%2
        # print("tempRet", tempRet)
        carry = (tempA + tempB + carry)/2
        # print("carry", carry)
        ret += str(tempRet)
        # print("ret", ret)
    for i in range(m,n):
        tempA = int(A[i])
        print("tempA", tempA)
        print("carry", carry)
        tempRet = (tempA + carry)%2
        print("tempRet", tempRet)
        carry = (tempA + carry)/2
        print("carry", carry)
        ret += str(tempRet)
        print("ret", ret)

    if carry == 1:
        ret += "1"
    ret = ret[::-1]
    i = 0
    while i < len(ret):
        if ret[i] != 0:
            break
        i += 1
    return ret[i:]


A = 1

B = 1

1

A = "100"
B = "11"

addBinary(A, B)