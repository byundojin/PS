from __future__ import annotations
import sys
from dataclasses import dataclass
ips = lambda:map(int, sys.stdin.readline().split())
N, Q = ips()

@dataclass(slots=True)
class Node:
    value:list[int]
    range_left:int
    range_right:int
    left:Node
    right:Node
    
    @property
    def len(self):
        return self.range_right - self.range_left + 1
    
    @property
    def is_leaf(self):
        return self.len == 1
    
    def is_in(self, index):
        return self.range_left <= index <= self.range_right
    
    def set(self, index, value):
        if self.is_leaf:
            self.value = [1, value]
            return

        self.value[0] += 1
        self.value[1] += value

        if self.left.is_in(index):
            self.left.set(index, value)
        else:
            self.right.set(index, value)
    
    def delete(self, index):
        if self.is_leaf:
            v = self.value[1]
            self.value = [0, 0]
            return v

        self.value[0] -= 1

        if self.left.is_in(index):
            v = self.left.delete(index)
        else:
            v = self.right.delete(index)
        
        self.value[1] -= v
        return v

    def get(self, value:int) -> int:
        if self.value[1] < value:
            return -1

        if self.is_leaf:
            r = self.value[0]
            return r 

        lv = self.left.value
        if lv[1] < value:
            r = self.right.get(value - lv[1])
            r += lv[0]
        else:
            r = self.left.get(value)

        return r

    @staticmethod
    def create(range_left, range_right):
        len = range_right - range_left + 1
        
        node = Node([0, 0], range_left, range_right, None, None)
        if len == 1:
            return node

        left_len = range_left + (len - (len // 2)) -1 

        node.left = Node.create(range_left, left_len)
        node.right = Node.create(left_len+1, range_right)
        return node
    
root = Node.create(1, N)
li = [[v, None] for v in ips()]
for idx, v in enumerate(sorted(li, reverse=True, key=lambda v: v[0])):
    idx += 1
    v[1] = idx
    root.set(idx, v[0])

# print(li)
arrows = sorted(
    enumerate(tuple(ips()) for _ in range(Q)),
    reverse=True,
    key=lambda v: v[1][0]
)
# print(arrows)

result = [-2] * Q
mx = N
for arrow in arrows:
    # print("------------")
    idx, v = arrow
    x, p = v
    # print(idx, x, p)
    while x < mx:
        _, i = li[mx-1]
        # print(f"delete {i}")
        root.delete(i)
        mx -= 1
    
    r = root.get(p)
    # print(idx, r)
    result[idx] = r
    # print("------------")

for r in result:
    print(r)