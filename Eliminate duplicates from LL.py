"""class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def delet(head, i):
    if i < 0 or i >= length(head):
        return head

    if i == 0:
        head = head.next
        return head
    smallHead = delet(head.next, i-1)
    head.next = smallHead
    return head

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

def append(head, n):
    newHead = head
    prev = None
    len = length(head)
    i = len - n
    for e in range(0, i):
        prev = newHead
        newHead = newHead.next
    prev.next = None
    tail = newHead
    while tail.next is not None:
        tail = tail.next
    tail.next = head
    return newHead

def eleminate_duplicate(head):
    tail = head
    prev = head
    after = head

    while after.next is not None:
        if after.next.data > prev.data:
            after = after.next
            prev = after
            tail.next = prev
            tail = prev
        else:
            after = after.next
    return head



user_input = input()
list = [int(e) for e in user_input.split(" ")]
head = createLL(list[:-1])
head = eleminate_duplicate(head)
printLL(head)

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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

def eleminate_duplicate(head):
    t1 = head
    t2 = head.next
    while t2 is not None:
        if t1.data != t2.data:
            t1.next = t2
            t1 = t2
            t2 = t2.next
        else:
            t2 = t2.next
    t1.next = t2
    return head

user_input = input()
list = [int(e) for e in user_input.split(" ")]
head = createLL(list[:-1])
head = eleminate_duplicate(head)
printLL(head)