
# contruct the trie
class TrieNode:
    def __init__(self, char=None):
        self.char = None
        self.child = {} 
        self.count = 0
        pass

class Trie:
    def __init__(self):
        self.root = TrieNode("*")
    
    def insertWordInTrie(self, word):
        # word = 'zebra'
        curr_node = self.root
        for char in word:
            if char not in curr_node.child:
                curr_node.child[char] = TrieNode(char)
            curr_node.count += 1
            curr_node = curr_node.child[char]

    # findUniquePrefix
    def findUniquePrefix(self, word):
        curr_node = self.root
        prefixWord = ""
        for char in word:
            prefixWord += char
            if curr_node.child[char].count == 1:
                break
            curr_node = curr_node.child[char]
        return prefixWord 



def shortestUniquePrefix(A):
    trie = Trie()

    for word in A:
        trie.insertWordInTrie(word)
    
    prefixList = []

    for word in A:
        shortestUniquePrefixWord = trie.findUniquePrefix(word)
        prefixList.append(shortestUniquePrefix)
    
    return prefixList
    
    
    return 0


A = ["zebra", "dog", "duck", "dove"]
# A = ["apple", "ball", "cat"]
shortestUniquePrefix(A)


A = [1, 2, 3, 4, 5]

class TrieNode:
    def __init__(self):
        self.val = 0
        self.child = {} 
        pass

class Trie:
    def __init__(self):
        self.root = TrieNode("*")
    
    def insertNumberInTrie(self, num):
        curr_node = self.root
        bin_num = bin(num)
        bin_num_len = len(bin_num)
        for i in range(bin_num_len, -1, -1):
            val = 1 if num & (1 << i) else 0
            if val not in curr_node.child:
                curr_node.child[val] = TrieNode(val)
            curr_node = curr_node.child[val]
        curr_node.val = num 
    
    
