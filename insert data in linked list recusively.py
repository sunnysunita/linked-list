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

def insert(head, i, data):
    if i < 0 or i > length(head):
        return head

    elif i == 0:
        newNode = Node(data)
        newNode.next = head
        return newNode

    smallHead = insert(head.next, i-1, data)
    head.next = smallHead
    return head


def createLL(list):
    head = Node(list[0])
    tail = head
    for e in list[1:]:
        newNode = Node(e)
        tail.next = newNode
        tail = newNode
    return head

def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    print()


list = [1,2,3,4,5,6,7]
i = -1
data = 8
head = createLL(list)
head = insert(head, i, data)
printLL(head)