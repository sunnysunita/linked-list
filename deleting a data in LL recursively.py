class Node:
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

user_input = input()
list = [int(e) for e in user_input.split(" ")]
i = int(input())
head = createLL(list[:-1])
head = delet(head, i)
printLL(head)