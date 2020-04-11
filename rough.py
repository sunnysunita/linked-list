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
    return [head, tail]


def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    print()

def reverseLL(head):
    if head.next is None:
        return head,head
    smallHead,tailhead = reverseLL(head.next)

    tailhead.next = head
    head.next = None
    return smallHead,head


user_input = input()
list = [int(e) for e in user_input.split(" ")]
head_tail = createLL(list[:-1])
head = head_tail[0]
tail = head_tail[1]
head,head1 = reverseLL(head)
printLL(head)