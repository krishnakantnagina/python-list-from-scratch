import ctypes

class MeraList:
    def __init__(self):
        self.size = 1
        self.n = 0

        #create a Ctype array with size = self.size
        self.A = self.__make_array(self.size)

    def __make_array(self,capacity):
        #create a Ctype array(static, referential) with size capacity
        return (capacity*ctypes.py_object)()
    
    #use magic method for create length check method
    def __len__(self):
        return self.n
    
    
    def append(self, item):
        #check array is empty or not 
        if self.size == self.n:
            #resize the array
            self.__resize(self.size*2)
        
        #append
        self.A[self.n]=item
        self.n = self.n + 1
        
    def __resize(self, new_capacity):
        #create a new array with new capacity
        B = self.__make_array(new_capacity)
        self.size=new_capacity
        #copy content of A to B
        for i in range(self.n):
            B[i]=self.A[i]
        #reassign A
        self.A = B