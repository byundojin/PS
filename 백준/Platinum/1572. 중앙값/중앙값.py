from __future__ import annotations
from dataclasses import dataclass
import sys
from collections import deque
ip = lambda:int(sys.stdin.readline())
ips = lambda:map(int, sys.stdin.readline().split())

N, K = ips()

@dataclass
class Node:
    # count, left, right
    value:int
    range_left:int
    range_right:int
    left:Node|None = None
    right:Node|None = None
    
    @property
    def is_leaf(self):
        return self.len == 1
    
    @property
    def len(self):
        return self.range_right - self.range_left + 1
    
    def get(self, gap=0, v=None):
        if v is None:
            v = (self.value+1)//2
        if self.is_leaf:
            return self.range_left

        if v <= self.left.value+gap:
            return self.left.get(gap, v)
        else:
            return self.right.get(gap+self.left.value, v)

    def add(self, index, value):
        if index < self.range_left or self.range_right < index:
            return
        self.value += value
        
        if self.left:
            self.left.add(index, value)
        if self.right:
            self.right.add(index, value)

    @staticmethod
    def create(range_left, range_right):
        len = range_right - range_left + 1
        
        if len == 0:
            return None

        node = Node(0, range_left, range_right)
        if len == 1:
            return node

        left_len = range_left + (len - (len // 2)) -1 

        node.left = Node.create(range_left, left_len)
        node.right = Node.create(left_len+1, range_right)
        return node
    
    def print(self):
        print(self.range_left, self.range_right, self.value)
        if self.left:
            self.left.print()
        if self.right:
            self.right.print()
    
root = Node.create(0, 65536)
queue = deque([])
for _ in range(K):
    v = ip()
    queue.append(v)
    root.add(v, 1)
res = root.get()
for _ in range(N-K):
    idx = queue.popleft()
    root.add(idx, -1)
    v = ip()
    queue.append(v)
    root.add(v, 1)
    res += root.get()
print(res)