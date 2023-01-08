

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# first = Node(3)
# print(first.data)

class LinkedList:
    def __init__(self):
        self.head = None


    def insert(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
    
    def printLL(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next




# ll = LinkedList()
# A = [1,2,3,4,5,6,7,8,9]

# for i in range(0, len(A)):
#     ll.insert(A[i])

# ll.printLL()




def deleteNodeIntheMiddle(A):
    if A is None:
        return None

    if A.next.next is None:
        A.next = None
        return A

    prev = None
    slow, fast = A, A

    while(fast and fast.next):
        prev = slow
        slow = slow.next
        fast = fast.next.next

    prev.next = prev.next.next

    return A


def reverseLinkedList(A):
    if A is None:
        return None
    
    if A.next is None:
        return A
    
    p1 = A
    p2 = A.next

    while(p2.next and p2):
        temp = p2.next    
        p2.next = p1
        p1 = p2
        p2 = temp
    return p1


ll = LinkedList()
A = [1,2,3,4,5,6]

for i in range(0, len(A)):
    ll.insert(A[i])


# print(ll.head.next)

w = reverseLinkedList(ll.head)







