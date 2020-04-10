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


def printRR(head):
    if head.next is None:
        print(head.data, end=" ")
        return head
    smallHead = printRR(head.next)
    head.next = smallHead
    print(head.data, end=" ")
    return head

user_input = input()
list = [int(e) for e in user_input.split(" ")]
head_tail = createLL(list[:-1])
head = head_tail[0]
tail = head_tail[1]
printRR(head)