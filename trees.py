'''
A tree will have a nodes, with value of left, right and value

It will first contain a root node

So first I will need to make a root node with left node and right node 

     3
    / \
   1   2 
   /\  /\
   n n n n



'''

from collections import deque


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



root = Node()
root.val = 3
root.left = Node(1, None, None)
root.right = Node(2, None, None)





def inOrderTraversal(A):
    arr = []
    stack = []
    while(A or stack):
        if A:
            stack.append(A)
            A = A.left
        else:
            A = stack.pop()
            arr.append(A.val)
            A = A.right
            

    return arr




def levelOrderTraversal(A):
    if not root:
        return []
    
    res = []
    queue = deque()
    queue.append(root)
    queue.append(None)

    while(queue):
        arr = []
        node = queue.popleft()
        if node:
            arr.append(node.val)
        else:
            res.append(arr)
            queue.append(None)
            continue
        
        if node.left:
            queue.append(node.left) 
        if node.right:
            queue.append(node.right)

    return res


