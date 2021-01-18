from binary_tree import Node
import time

#
def print_pretty(root): 
      
    # Base case 
    if root is None: 
        return
    # Create an empty queue for level order traversal 
    q = [] 
      
    
    q.append(root) 
    depth = root.getHeight()
    while q: 
      
        
        count = len(q) #Num of nodes on current level
        
        
      
        while count > 0: 
            temp = q.pop(0) 
            print(depth * ' ' + str(temp.data), end = '  ') 
            time.sleep(3)
            if temp.left: 
                q.append(temp.left) 
            if temp.right: 
                q.append(temp.right) 
            depth -= 1
            count -= 1
        print(' ') 
    

root = Node(25)
root.insert(12)
root.insert(10)
root.insert(22)
root.insert(5)
root.insert(36)
root.insert(30)
root.insert(40)
root.insert(28)
root.insert(38)
root.insert(48)

print_pretty(root)
