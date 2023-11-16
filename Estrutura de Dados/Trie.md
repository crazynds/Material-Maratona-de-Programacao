# Trie

> A trie (derived from retrieval) is a multiway tree data structure used for storing strings over an alphabet. It is used to store a large amount of strings. The pattern matching can be done efficiently using tries.

<img src="./Triedatastructure1.png" height=400/>

Tem custo fixo de $O(M)$ para suas operações, sendo $M$ o tamanho da string de entrada.

Possui diversas variações, sendo algumas delas:
- [binary trie](./BinaryTrie.md)
- compressed trie
- [ternary search tree](https://en.wikipedia.org/wiki/Ternary_search_tree)


## Python - [Trie](https://www.geeksforgeeks.org/trie-insert-and-search/)


```python

class TrieNode:
     
    # Trie node class
    def __init__(self):
        self.children = [None]*26
 
        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False
 
class Trie:
     
    # Trie data structure class
    def __init__(self):
        self.root = TrieNode()
 
    def _charToIndex(self,ch):
        return ord(ch)-ord('a')
 
 
    def insert(self,key):
        node = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
 
            if not node.children[index]:
                node.children[index] = self.getNode()
            node = node.children[index]
 
        # mark last node as a complete word
        node.isEndOfWord = True
 
    def search(self, key):
        node = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not node.children[index]:
                return False
            node = node.children[index]
 
        return node.isEndOfWord
```