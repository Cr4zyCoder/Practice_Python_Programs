class Queue:
    def _init_(self,max_size):
        self.__max_size=max_size
        self._elements=[None]*self._max_size
        self.__rear=-1
        self.__front=0
    def is_full(self):
        if(self._rear==self._max_size-1):
            return True
        return False
    def is_empty(self):
        if(self._front>self._rear):
            return True
        return False
    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full")
        else:
            self.__rear+=1
            self._elements[self._rear]=data
    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty")
        else:
            data=self._elements[self._front]
            self.__front+=1
            return data
    def display(self):
        for index in range(self._front, self._rear+1):
            print(self.__elements[index])
    def get_max_size(self):
        return self.__max_size
queue1=Queue(4)
print("Is it full",queue1.is_full())
print("Is it empty",queue1.is_empty())
queue1.enqueue(100)
queue1.display()
queue1.enqueue(200)
queue1.enqueue(300)
queue1.enqueue(400)
queue1.display()
queue1.enqueue(500)