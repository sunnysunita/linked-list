class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find(head, data):
    count = 0
    while head is not None:
        if head.data == data:
            return count
        count += 1
        head = head.next
    return -1


def length(head):
    len = 0
    temp = head
    while temp is not None:
        len += 1
        temp = temp.next
    return len


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
data = int(input())
head = createLL(list[:-1])
print(find(head, data))
