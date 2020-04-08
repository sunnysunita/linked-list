class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


a = Node(10)
b = Node(20)
print(a.data)
print(b.data)
a.next = b  # referencing node a with b

print(a.next.data)
# print(b.next.data)
