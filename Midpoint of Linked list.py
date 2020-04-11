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
def printRR(head):
    if head.next is None:
        print(head.data, end=" ")
        return head
    smallHead = printRR(head.next)
    head.next = smallHead
    print(head.data, end=" ")
    return head
def countLL(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count

def midpoint(head):
    count = countLL(head)
    if count % 2 == 0:
        even = count // 2
        temp = head
        for i in range(1, even):
            temp = temp.next
        print(temp.data)

    else:
        odd = count // 2
        temp = head
        for i in range(0, odd):
            temp = temp.next
        print(temp.data)

user_input = input()
list = [int(e) for e in user_input.split(" ")]
head = createLL(list[:-1])
midpoint(head)