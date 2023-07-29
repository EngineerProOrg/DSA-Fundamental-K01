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
        
     
    def merge(self, list_2: DLinkedList):
        # self: list_1 
        # new_list = list_1 -> list_2
        
        # HEAD_1 -> A -> B -> TAIL_1 (list_1)
        # HEAD_2 -> D -> E -> TAIL_2  (list_2)
        tail_prev = self.__tail.prev  # B
        head_next = list_2.get_head().next # D
        
        tail_prev.next = head_next
        head_next.prev = tail_prev
        
        # HEAD_1 -> A -> B -> D -> E -> TAIL_2 
        # self.__tail = TAIL_1 
        self.__tail = list_2.get_tail()
        # self.__tail = TAIL_2


    
l = DLinkedList()

l.push_back(10)
l.push_back(20)
l.push_back(30)
l.push_back(50)
l.push_back(60)

print("Printing list 1")
l.pprint()

l2 = DLinkedList()
l2.push_back(-100)
l2.push_back(-200)

print("Printing list 2")

print("Merging 2 Lists")
l2.pprint()
l.merge(l2)
print("Printing merged linked list")
l.pprint()

# l1, l2 = l.partition(l.index(2))
# l1.pprint()
# l2.pprint()

# Output
# Printing list 1
# 10
# 20
# 30
# 50
# 60
# End
# _________________________
# Printing list 2
# Merging 2 Lists
# -100
# -200
# End
# _________________________
# Printing merged linked list
# 10
# 20
# 30
# 50
# 60
# -100
# -200
# End
# _________________________
