# Singly linked list
class Node:
    value = None 
    next = None
    
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next 
        
        
class LinkedList:
    __head = None
    
    def __init__(self):
        self.__head = Node() # None
        
    def get_head(self):
        return self.__head
    
        
    def pprint(self):
        cur_node = self.__head.next 
        print("Printing linked list ...")
        while cur_node is not None:
            print(cur_node.value)
            cur_node = cur_node.next
        print("End")
        
    
    def insert(self, value):
        # Add new node to the front of the linked list
        
        # HEAD -> B ->C -> NULL
        head = self.__head
        next_node = head.next # node B
        # Insert new node - node A         
        new_node = Node(value=value)
        new_node.next = next_node
        # HEAD   A -> B : No link between HEAD and A
        head.next = new_node
        # HEAD -> A -> B -> C -> NULL

        # Corner case: Empty linked list
        #    HEAD -> NULL
        #    next_node = HEAD.next = NULL
        #    new_node = Node A 
        #    HEAD -> A -> NULL
        
    def index(self, idx):
        cur_node = self.__head.next
        cnt = 0
        
        while cur_node is not None:
            cnt += 1
            if cnt == idx:
                return cur_node
            
            cur_node = cur_node.next
    
        print("Out of range")
        return None
    
    
    def get_tail(self):
        # HEAD -> A -> B -> C -> NULL
        # return C - tail is the last Non-NULL node
        cur_node = self.__head
        while cur_node.next is not None:
            cur_node = cur_node.next
        
        return cur_node
    
    def delete(self, delnode: Node):
        # HEAD -> A -> B -> C -> NULL
        # Example: delnode = B
        
        next_node = delnode.next # Node C
        
        previous_node = self.__head
        while previous_node.next != delnode:
            previous_node = previous_node.next
        # previous_node = node A
        
        previous_node.next = next_node
        delnode = None
        
        
        
l = LinkedList()
l.insert(10)
l.insert(2)
l.insert(15)
l.insert(100)
l.insert(200)
l.pprint()
print("---------------------------")
print("Deleting node at index 3")
l.delete(l.index(3))
l.pprint()
print("---------------------------")


# Output
# Printing linked list ...
# 200
# 100
# 15
# 2
# 10
# End
# ---------------------------
# Deleting node at index 3
# Printing linked list ...
# 200
# 100
# 2
# 10
# End
# ---------------------------
