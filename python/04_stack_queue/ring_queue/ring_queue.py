class RingQueue:
    def __init__(self, len):
        self.queue = [0 for _ in range(len)]
        self.front = 0
        self.rear = 0

    def is_full(self):
        return self.front == (self.rear + 1) % self.size()

    def is_empty(self):
        return self.front == self.rear

    def enqueue(self, n):
        if self.is_full():
            print('> can not enqueue')
            return
        
        self.queue[self.rear] = n
        self.rear = (self.rear + 1) % self.size()

    def dequeue(self):
        if self.is_empty():
            print('> can not dequeue')
            return
        self.front = (self.front + 1) % self.size()

    def index(self, key):
        i = self.front
        while i != self.rear:
            if self.queue[i] == key:
                return (i - self.front) % self.size()
            i = (i + 1) % self.size()

        return -1
    def size(self):
        return len(self.queue)
    
    def to_list(self):
        list = []
        i = self.front
        while i != self.rear:
            list.append(self.queue[i])
            i = (i + 1) % self.size()
        return list

print(':: init ring queue')
ring_queue = RingQueue(10)
print(ring_queue.is_empty()) # True
print(ring_queue.is_full()) # False

print(':: enqueue')
ring_queue.enqueue(10)
ring_queue.enqueue(20)
ring_queue.enqueue(30)
print(ring_queue.is_empty()) # False

print(':: dequeue')
ring_queue.dequeue()

print(':: index')
print(ring_queue.index(10)) # -1
print(ring_queue.index(20)) # 1

print(':: to list')
print(ring_queue.to_list()) # [20, 30]

print(':: is full')
ring_queue.enqueue(1)
ring_queue.enqueue(2)
ring_queue.enqueue(3)
ring_queue.enqueue(4)
ring_queue.enqueue(5)
ring_queue.enqueue(6)
print(ring_queue.is_full()) # False
ring_queue.enqueue(7)
print(ring_queue.is_full()) # True
ring_queue.enqueue(8)
print(ring_queue.is_full()) # True