class Node:
    def __init__(self, data, prev=None):
        self.__data = data
        self.__prev = prev
        
    def __get_prev(self):
        return self.__prev
    
    def __set_prev(self, ref):
        self.__prev = ref
        
    def __get_data(self):
        return self.__data
    
    def __set_data(self, data):
        self.__data = data
        
    data = property(__get_data, __set_data)
    prev = property(__get_prev, __set_prev)

class Queue:
    
    def __init__(self):
        self.count = 0
        
        self.head = None
        self.tail = None
    
    def push(self, data):
        n = Node(data)
        if self.count == 0:
            self.head = n
        else:
            self.tail.prev = n
        self.tail = n
        self.count += 1
            
    def pop(self):
        if self.count == 0:
            return None
        buf_data = self.head.data
        self.head = self.head.prev
        self.count -= 1
        return buf_data
    
    def show(self):
        if self.count != 0:
            return self.head.data
        return None