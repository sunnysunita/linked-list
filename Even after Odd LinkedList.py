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



def countLL(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count


def oddLL(head):
    h1 = Node(-1)
    tail = h1
    tail.next = None
    odd = head
    while odd is not None:
        if odd.data %2 != 0:
            newNode = Node(odd.data)
            tail.next = newNode
            tail = newNode
            tail.next = None
        odd = odd.next
    h2 = evenLL(head)
    tail.next = h2
    return h1.next

def evenLL(head):
    h1 = Node(-1)
    tail = h1
    tail.next = None
    even = head
    while even is not None:
        if even.data %2 == 0:
            newNode = Node(even.data)
            tail.next = newNode
            tail = newNode
            tail.next = None
        even = even.next
    return h1.next






user_input = input()
list0 = [int(e) for e in user_input.split(" ")]
head = createLL(list0[:-1])
h1 = oddLL(head)

printLL(h1)


