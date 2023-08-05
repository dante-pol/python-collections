class Node:
    def __init__(self, data, next_ref=None):
        self.data = data 
        self.next = next_ref

class LinkedList:
    
    def __init__(self):
        self.__count = 0
        self.__head = None
        self.__tail = None
    
    
    def __getitem__(self, key):
        pass
    
    
    def __add__(self):
        pass
    
    
    def __sub__(self):
        pass
    
    
    def add(self, item) -> None:
        n = Node(data=item)
        if self.is_empty():
            self.__head = n
        self.__tail.next = n
        self.__tail = n
    
    def remove(self, index) -> bool:
        if self.is_empty():
            return False
        
        if index < 0 or index > self.count - 1:
            return False
        
        count = 0
        t_prev = self.__head
        
        while count != index - 1:
            t_prev = t_prev.next
            count += 1
        
        target = t_prev.next
        t_next = target.next
        
        t_prev.next = t_next
        
    
    
    def find(self, item) -> int:
        pass
    
    
    def insert(self, item, index) -> None:
        pass
    
    
    def is_empty(self) -> bool:
        pass