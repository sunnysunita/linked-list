from sys import setrecursionlimit
setrecursionlimit(11000)
class Node:
    def __init__(self,data):
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

def reverseLL(head):
    if head.next is None:
        return head
    smallHead = reverseLL(head.next)

    tail = head.next
    tail.next = head
    tail = tail.next
    head.next = None
    return smallHead


user_input = input()
list = [int(e) for e in user_input.split(" ")]
head = createLL(list[:-1])
printLL(head)

head = reverseLL(head)
printLL(head)