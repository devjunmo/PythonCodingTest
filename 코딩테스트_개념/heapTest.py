import heapq

class PriorityQueue:
    def __init__(self, max_heap):
        self._heap = [-i for i in max_heap]
        heapq.heapify(self._heap)

    def push(self, item):
        heapq.heappush(self._heap, -item)

    def pop(self):
        return -heapq.heappop(self._heap)

    def peek(self):
        return -self._heap[0]

    def __len__(self):
        return len(self._heap)

lst = [1, 4, 5,2,10,9]

pq = PriorityQueue(lst) 

print(pq._heap) # [-10, -4, -9, -2, -1, -5]

pq.peek() # 10
pq.pop() # 10
pq._heap # [-9, -4, -5, -2, -1]
