import sys
from collections import *

class Underflow(Exception):
    pass  # make it fancier if you want :)

class MinHeap:
    def __init__(self):
        self.heap = [0]
        self.count = 0

    def size(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def look(self):
        if self.is_empty():
            raise Underflow("HeapError")
        return self.heap[1]

    def to_string(self):
        if self.is_empty():
            return("Empty")
        else:
            heap = self.heap[1:self.size()+1]
            st = ''
            for i in heap:
                st += str(i)
                st+= ' '
            return st.strip()

    def heapDecreaseKey(self, i):
        while i // 2 > 0:
            parent,child = i // 2,i
            if self.heap[child] < self.heap[parent]:
                self.heap[parent], self.heap[child] = self.heap[child],self.heap[parent]
            i = parent

    def heapify(self,i):
        child = i
        while 2*child <= self.count:
            if self.heap[child] > self.heap[self.minChild(i)]:
                self.heap[child], self.heap[self.minChild(i)] = self.heap[self.minChild(i)], self.heap[child]
            child = self.minChild(i)

    def minChild(self,i):
        child = 2*i
        if child + 1 > self.count:
            return child
        if self.heap[child] < self.heap[child+1]:
            return child
        return child + 1

    def insert(self,x):
        self.heap.append(x)
        self.count += 1
        self.heapDecreaseKey(self.count)

    def remove(self):
        if self.is_empty():
            raise Underflow("HeapError")
        rem = self.heap[1]
        self.heap[1] = self.heap[self.count]
        self.count = self.count - 1
        self.heap.pop()
        self.heapify(1)
        return rem

def driver():
    heap = MinHeap()
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            in_data = f.readline().strip().split()
            action, value_option = in_data[0], in_data[1:]
            if action == "print":
                print(heap.to_string())
            elif action == "insert":
                heap.insert(int(value_option[0]))
            elif action == "size":
                print(heap.size())
            elif action == "best":
                try:
                    print(heap.look())
                except Underflow:
                    print("HeapError")
            elif action == "remove":
                try:
                    print(heap.remove())
                except Underflow:
                    print("HeapError")

if __name__ == "__main__":
    driver()
