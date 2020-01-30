import sys
sys.path.append('queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        newNode = BinarySearchTree(value)
        current = self
        while True:
            if value < current.value: 
                if current.left == None: 
                    current.left = newNode
                    return
                else: 
                    current = current.left    
            elif value > current.value: 
                if current.right == None: 
                    current.right = newNode
                    return
                else: 
                    current = current.right

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
            else: 
                return False    
        elif target > self.value:
            if self.right:
                return self.right.contains(target)
            else: 
                return False 

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right == None: 
            return self.value
        else: 
            return self.right.get_max()    
            

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        if self.right != None and self.left != None:
            cb(self.value)
            self.left.for_each(cb)
            return self.right.for_each(cb)      
        if self.right == None and self.left != None:
            cb(self.value)
            return self.left.for_each(cb)    
        if self.right != None and self.left == None:
            cb(self.value)
            return self.right.for_each(cb) 
        if self.right == None and self.left == None:
            cb(self.value)
            return      
            
    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        def traverse(n):
            if n.left: 
                traverse(n.left)
            print(n.value)
            if n.right:
                traverse(n.right)
        traverse(self)
        return             


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)
        while queue.len() > 0:
            temp = queue.dequeue()
            print(temp.value)
            if temp.left:
                queue.enqueue(temp.left)
            if temp.right: 
                queue.enqueue(temp.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        while stack.len() > 0:
            temp = stack.pop()
            print(temp.value)
            if temp.left:
                stack.push(temp.left)
            if temp.right: 
                stack.push(temp.right)
  


    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        def traverse(n):
            print(n.value)
            if n.left: 
                traverse(n.left)
            if n.right:
                traverse(n.right)
        traverse(self)
        return  

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        def traverse(n):
            if n.left: 
                traverse(n.left)
            if n.right:
                traverse(n.right)
            print(n.value)    
        traverse(self)
        return  



tree = BinarySearchTree(5)

tree.insert(2)

tree.insert(6)
tree.insert(1)
tree.insert(7)
tree.insert(3)
tree.insert(8)


arr = []
cb = lambda x: arr.append(x)

#print(tree.dft_print(BinarySearchTree(5)))


