
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
                print('left')
                return self.left.contains(target)
            else: 
                return False    
        elif target > self.value:
            if self.right:
                print('right')
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
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass



tree = BinarySearchTree(5)

tree.insert(6)

tree.insert(7)



#print(tree.right.right.right.value)

print(tree.get_max())