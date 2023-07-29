class DNode:
    value = None 
    prev = None
    next = None 
    
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev
    
class DLinkedList:
    def __init__(self):
        self.__head = DNode()
        self.__tail = DNode()
        
        self.__head.next = self.__tail
        self.__tail.prev = self.__head
        
    def get_head(self):
        return self.__head
    
    def get_tail(self):
        return self.__tail
    
    def pprint(self):
        cur_node = self.__head.next 
        # HEAD Node(None) -> TAIL Node(None)
        
        while cur_node is not self.__tail:
            print(cur_node.value)
            cur_node = cur_node.next
        print("End")
        print("_________________________")
        
    def push_back(self, value):
        # HEAD A -> B -> C ->     D (new node)      TAIL
        tail_prev = self.__tail.prev # node C

        new_node = DNode(value) # node D
        
        tail_prev.next = new_node
        new_node.prev = tail_prev
        
        new_node.next = self.__tail 
        self.__tail.prev = new_node
        
    def push_front(self, value):
        # HEAD   A (new node) -> B -> C -> TAIL
        head_next = self.__head.next  # node B
        
        new_node = DNode(value) # node A
        
        self.__head.next = new_node
        new_node.prev = self.__head
        
        new_node.next = head_next 
        head_next.prev = new_node
        
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
    
    def delete(self, delnode: DNode):
        #  HEAD -> A -> B -> C -> TAIL   delnode = B 
        prev_node = delnode.prev  # A
        next_node = delnode.next  # C
        
        prev_node.next = next_node
        next_node.prev = prev_node    
        delnode = None

    def reverse(self):
        # HEAD -> A -> B -> C -> D -> TAIL

        cur_node = self.__head.next
    
        while cur_node != self.__tail:
            # Save next_node to move the cursor
            next_node = cur_node.next
            
            #         prev -> cur_node
            # Expect: cur_node -> prev
            prev_node = cur_node.prev
            
            cur_node.next = prev_node
            prev_node.prev = cur_node
            cur_node.prev = next_node
            
            cur_node = next_node
            
        # Swap TAIL.prev <-> TAIL.next
        prev_tail = self.__tail.prev
        self.__tail.next = prev_tail
        self.__tail.prev = None
        
        # Swap HEAD <-> TAIL
        head = self.__head
        self.__head = self.__tail
        self.__tail = head 

l = DLinkedList()

l.push_back(10)
l.push_back(20)
l.push_back(30)
l.push_back(50)
l.push_back(60)
print("Print original list")
l.pprint()
l.reverse()
print("Print reversed list")
l.pprint()

# Output
# Print original list
# 10
# 20
# 30
# 50
# 60
# End
# _________________________
# Print reversed list
# 60
# 50
# 30
# 20
# 10
# End
# _________________________
