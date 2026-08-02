from collections import deque

q = deque()

q.append("A")
q.append("B")
q.append("C")

while q:
    print(q.popleft())