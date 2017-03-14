#Min Heap Implementation
#Author: Matt Broe

import random

class minHeap:

    def __init__(self, size = None):
        
        if size == None:
            self.data = [None]*50
            self.size = 50
            self.increment = 50
            self.numElements = 0
            self.tail = 0

        else:        
            self.data = [None]*size
            self.size = size
            self.increment = size
            self.numElements = 0
            self.tail = 0

    def siftUp(self, n):
        
        if 0 < n and n < self.numElements:
            current = n
            parent = (n-1)//2
        
            while current > 0 and self.data[current] < self.data[parent]:
                self.data[current], self.data[parent] = self.data[parent], self.data[current]
                current = parent
                parent = (current-1)//2

    def siftDown(self, n):
        
        if 0 <= n and n < self.numElements:
            current = n
            leftChild = (2*n) + 1
            rightChild = (2*n) + 2

            while leftChild < self.size and self.data[leftChild] != None:
                
                minChild = leftChild
                
                if rightChild < self.size and self.data[rightChild] != None:
                    if self.data[leftChild] > self.data[rightChild]:
                        minChild = rightChild
                
                if self.data[current] > self.data[minChild]:
                    self.data[current], self.data[minChild] = self.data[minChild], self.data[current]
                    current = minChild
                    leftChild = (2*current) + 1
                    rightChild = (2*current) + 2

                else:
                    break

    def push(self, x):
        
        if self.numElements == self.size:
            self.data += [None]*(self.increment)
            self.size += self.increment
        self.data[self.tail] = x
        self.numElements += 1
        self.siftUp(self.tail)
        self.tail += 1

    def getMin(self):
        return self.data[0]

    def pop(self):
        if self.numElements > 0:
            self.data[0], self.data[self.tail-1] = self.data[self.tail-1], self.data[0]
            root = self.data[self.tail-1]
            self.data[self.tail-1] = None
            self.numElements -= 1
            self.tail -= 1
            self.siftDown(0)
            return root

    
    

    
    
