# AVL Tree

A arvore AVL é uma arvore binária que implementa um algoritmo que mantém a arvore balanceada. Como a arvore se mantém balanceada é ótimo para executar consultas em tempo $log N$.

Inserção: O(log N)  
Remoção: O(log N)  
Espaço: O(N)

Esse tipo de arvore de acordo com o algoritmo as chaves podem ser únicas, ou podem repetir. Nas arvores binárias podem otimizar consultas (min, max, search, etc...) em tempo $log N$ com caches em cada nó.


# Python - AVL Tree

Implementação que permite chaves duplicas.

```python
# Create a tree node
class TreeNode():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

    # Get the height of the node
    def getHeight(self):
        return self.height

    # Get balance factore of the node
    def getBalance(self):
        return (self.left.getHeight() if self.left else 0) - (self.right.getHeight() if self.right else 0)

    def getMinValueNode(self):
        if not self.left:
            return self
        return self.left.getMinValueNode()
    
        # Function to perform left rotation
    def leftRotate(self):
        y = self.right
        temp = y.left
        y.left = self
        self.right = temp
        self.height = 1 + max(self.left.getHeight() if self.left else 0,
                           self.right.getHeight() if self.right else 0)
        y.height = 1 + max(y.left.getHeight() if y.left else 0,
                           y.right.getHeight() if y.right else 0)
        return y

    # Function to perform right rotation
    def rightRotate(self):
        if not self.left:
            return self
        y = self.left
        temp = y.right
        y.right = self
        self.left = temp
        self.height = 1 + max(self.left.getHeight() if self.left else 0,
                           self.right.getHeight() if self.right else 0)
        y.height = 1 + max(y.left.getHeight() if y.left else 0,
                           y.right.getHeight() if y.right else 0)
        return y

    def insert_node(self, key):

        # Find the correct location and insert the node
        if key < self.key:
            self.left = self.left.insert_node(key) if self.left else TreeNode(key)
        else:
            self.right = self.right.insert_node(key) if self.right else TreeNode(key)

        self.height = 1 + max(self.left.getHeight() if self.left else 0,
                              self.right.getHeight() if self.right else 0)

        # Update the balance factor and balance the tree
        balanceFactor = self.getBalance()
        if balanceFactor > 1:
            if key < self.left.key:
                return self.rightRotate()
            else:
                self.left = self.left.leftRotate()
                return self.rightRotate()

        if balanceFactor < -1:
            if key > self.right.key:
                return self.leftRotate()
            else:
                self.right = self.right.rightRotate()
                return self.leftRotate()

        return self

    # Function to delete a node
    def delete_node(self, key):

        if key < self.key:
            self.left = self.left.delete_node(key) if self.left else None
        elif key > self.key:
            self.right = self.right.delete_node(key) if self.right else None
        else:
            if self.left is None:
                temp = self.right
                self = None
                return temp
            elif self.right is None:
                temp = self.left
                self = None
                return temp
            temp = self.right.getMinValueNode()
            self.key = temp.key
            self.right = self.right.delete_node(temp.key) if self.right else None
        if self is None:
            return self

        # Update the balance factor of nodes
        self.height = 1 + max(self.left.getHeight() if self.left else 0,
                              self.right.getHeight() if self.right else 0)

        balanceFactor = self.getBalance()

        # Balance the tree
        if balanceFactor > 1:
            if self.left.getBalance() >= 0:
                return self.rightRotate()
            else:
                self.left = self.left.leftRotate() if self.left else None
                return self.rightRotate()
        if balanceFactor < -1:
            if self.right.getBalance() <= 0:
                return self.leftRotate()
            else:
                self.right = self.right.rightRotate() if self.right else None
                return self.leftRotate()
        return self        
    
    def iterate(self,reverse= False):
        if reverse:
            if self.right:
                for key in self.right.iterate(reverse):
                    yield key
            yield self.key
            if self.left:
                for key in self.left.iterate(reverse):
                    yield key
        else:
            if self.left:
                for key in self.left.iterate(reverse):
                    yield key
            yield self.key
            if self.right:
                for key in self.right.iterate(reverse):
                    yield key
    
    def __str__(self):
        return str(self.key)



class AVLTree(object):

    def __init__(self) -> None:
        self.root = None
        pass

    def insert(self,value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self.root = self.root.insert_node(value)
    def delete(self,value):
        if not self.root:
            return None
        self.root = self.root.delete_node(value)

    def iterate(self,reverse= False):
        if not self.root:
            return range(0)
        return self.root.iterate(reverse)
```