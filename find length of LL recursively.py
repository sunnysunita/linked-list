class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def lengthRecursive(head):
    count = 0
    while head is not None:
        count +=1
        head = head.next
    return count

def ll(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
len=lengthRecursive(l)
print(len)