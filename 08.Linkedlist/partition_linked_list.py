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

    def partition(self, x: DNode): # Into 2 list [HEAD -> x]  and [x + 1 -> TAIL]
        if x == self.__head:
            return DLinkedList(), self
        if x == self.__tail or x == self.__tail.prev:
            return self, DLinkedList()    
        
        # HEAD -> A -> B -> C -> D -> TAIL
        # HEAD -> A -> x -> ....
        # .... -> C -> D -> TAIL 
        
        x_next = x.next # node C
        
        # Linked list 1 with HEAD1 and TAIL1
        l1 = DLinkedList() # HEAD1 -> A -> B(x) |-> C -> D ->| TAIL1
        l1.get_head().next = self.__head.next
        l1.get_head().next.prev = l1.get_head()
        
        x.next = l1.get_tail()
        l1.get_tail().prev = x 
        # HEAD1 -> A -> B(x) -> TAIL1 

        # Linkedlist 2 with HEAD2 and TAIL2
        l2 = DLinkedList() # HEAD2 -> C (x_next) -> D -> TAIL
        l2.get_head().next = x_next 
        x_next.prev = l2.get_head()
        
        prev_tail = self.__tail.prev # Node D 
        prev_tail.next = l2.get_tail() 
        l2.get_tail().prev = prev_tail

        return l1, l2

        
    
l = DLinkedList()

l.push_back(10)
l.push_back(20)
l.push_back(30)
l.push_back(50)
l.push_back(60)
l.push_back(-100)
l.push_back(-200)
print("Print original list")
l.pprint()
print("Partitioning at index 5")
l1, l2 = l.partition(l.index(5))
print("Print linked list 1")
l1.pprint()
print("Print linked list 2")
l2.pprint()

# Output
# Print original list
# 10
# 20
# 30
# 50
# 60
# -100
# -200
# End
# _________________________
# Partitioning at index 5
# Print linked list 1
# 10
# 20
# 30
# 50
# 60
# End
# _________________________
# Print linked list 2
# -100
# -200
# End
# _________________________
