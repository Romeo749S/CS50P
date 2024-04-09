class Jar:
    def __init__(self, capacity=12 ):
        self.capacity = capacity
        self._size = 0


    def __str__(self):
        return  '🍪' * self.size



    def deposit(self, n):
        self.n = n
        if self._size + self.n  > self.capacity:
            raise ValueError
        self._size = self._size + self.n

    def withdraw(self, n):
        self.n = n
        if self._size - self.n  < 0:
            raise ValueError
        self._size = self._size - self.n
 

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter 
    def capacity(self , capacity):
        if capacity < 0 or capacity/int(capacity) != 1:
            raise ValueError
        self._capacity = capacity


    @property
    def size(self):
        return self._size
    


def main():    
    jar = Jar(3)
    jar.deposit(3)
    jar.withdraw(1)
    print(jar)

if __name__ == '__main__':
    main()
    



    
    
