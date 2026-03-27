class CircularQueue:
    def __init__(self, n):
        self.size = n
        self.arr = [0]*n
        self.front = self.rear = -1

    def enqueue(self, x):
        if (self.rear + 1) % self.size == self.front:
            return "Full"
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.arr[self.rear] = x