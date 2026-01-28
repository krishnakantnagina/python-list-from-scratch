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

    def __str__(self):
        result =''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','
        #Remove last comma
        return '[' + result[:-1] + ']'
    
    def __getitem__(self,index):
        if 0 <= index < self.n:
            return self.A[index]
        else:
            return 'IndexError - Index out of range'
        
    def pop(self):
        if self.n==0:
            return print('Empty List')
        
        print(self.A[self.n-1])
        self.n = self.n - 1 #shortcut

    def clear(self):
        self.n = 0
        self.size = 1

    def find(self,item):
        for i in range(self.n):
            if self.A[i]==item:
                return i
            
        return "ValueError - not in list"
    
    def insert(self,pos,value):
        if self.n == self.size:
            self.__resize(self.size*2)

        for i in range(self.n, pos, -1):
            self.A[i] = self.A[i-1]

        self.A[pos]=value
        self.n = self.n + 1