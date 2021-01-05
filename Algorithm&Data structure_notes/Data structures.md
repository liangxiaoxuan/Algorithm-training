### Arrays

* A collection of elements/valus each identified by an array index or key  [0,1,2,3,4,5]
* Multidimensional array: matrixes (exp: [2][3]
* Disadvantages:
  1.Have to know the size of the array at compile-time <br>
  2.if it is full: have to create a bigger array and have to copy the values one by one <br>
  3.it is not able to store items with different types
  


### Binary Tree / Binary search tree
* Each node has at most two children
* Each root has tree parts: value-left-right 
* A value has two pointer: left&right
* Creating a Tree
```python
class Node:
    def __init__(self,val):
        self.left = None
        self.right = None 
        self.value = val
class Tree:
    def __init__(self):
        self.root - None

```
* Display Tree
```python
def PrintTree(self):
  if self.root != None:
    self._PrintTree(self.root)
    
def PrintTree(self,node):
  if node != None:
    self._PrintTree(node.left)
    print (str(node.value) + " ")
    self._PrintTree(node.right)

```
* Find Node
```python
def find(self,val):
    if self.root != None:
        return self._find(val,self.roo)
    else:
        return None

def find(self, val, node):
    if val == node.value:
        return node
    elif val < node.value and node.left != None:
        self._find(val, node.left)
    elif val > node.value and node.right != None:
        self._find(val,node.right)
```
* Insert Node 
```python
def add(self,val):
    if self.root == None:
        self.root = Node(val)
    else:
        self._add(val,self.root)
```







