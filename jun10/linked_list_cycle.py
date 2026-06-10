class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c
c.next = a

slow = fast = a

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
        print("Cycle Found")
        break