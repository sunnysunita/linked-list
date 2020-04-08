class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def length(head):
    len = 0
    temp = head
    while temp is not None:
        len += 1
        temp = temp.next
    return len

def ithNode(head, i):
    len=length(head)
    if i>=len:
        return None
    else:
        temp = head
        for e in range(0,i):
            temp=temp.next
        return temp
def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
i=int(input())
node = ithNode(l, i)
if node != None:
    print(node.data)
else:
    print("")