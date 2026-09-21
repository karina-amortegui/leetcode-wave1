'''
Doubly (Double Sided) Linked List

A normal singly linked list has: A → B → C
Each node only knows: node.next

A doubly linked list has:

A ⇄ B ⇄ C

Each node knows:

node.prev
node.next

Imagine we need to remove B.
Because B knows both neighbors:

A ⇄ B ⇄ C

we can directly connect:

A ⇄ C

Code:
node.prev.next = node.next
node.next.prev = node.prev

That's: O(1)
No searching required.

class ListNode:
    def init(self, val=0, next=None, prev=None):
        self.val = val
        self.prev = prev
        self.next = next

146) LRU cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

- LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
- int get(int key) Return the value of the key if the key exists, otherwise return -1.
- void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. 
If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Example 1:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 

Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.LRU = Node(0, 0)
        self.MRU = Node(0, 0)

        self.LRU.next = self.MRU
        self.MRU.prev = self.LRU
        
    def remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def add_node(self, node):
        prev_node = self.MRU.prev
        prev_node.next = node

        node.prev = prev_node
        node.next = self.MRU
        self.MRU.prev = node


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove_node(node)
        self.add_node(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        # if the key exists in self.cache, update the val
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove_node(node)
            self.add_node(node)
            return

        # if key not in self.cache
        if key not in self.cache:
            new_node = Node(key, value)
            self.add_node(new_node)
            self.cache[key] = new_node

        # if len(cache) > capacity, remove LRU node and from cache
        if len(self.cache) > self.capacity:
            lru_node = self.LRU.next
            self.remove_node(lru_node)
            del self.cache[lru_node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

'''