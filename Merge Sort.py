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





def reverseLL(head):
    curr = head
    prev = None
    next = None
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev





def merge(h1, h2):
    head = None
    tail = head
    if h1.data < h2.data:
        head = h1
        tail = head
        h1 = h1.next
    else:
        head = h2
        tail = head
        h2 = h2.next
    while h1 is not None and h2 is not None:
        if h1.data < h2.data:
            tail.next = h1
            tail = h1
            h1 = h1.next
        else:
            tail.next = h2
            tail = h2
            h2 = h2.next
    if h1 is not None:
        tail.next = h1

    if h2 is not None:
        tail.next = h2

    return head

def mergeSort(head):
    if head.next is None:
        return head
    else:
        count = countLL(head)
        midval = count // 2
        mid = head
        for i in range(1, midval):
            mid = mid.next
        h2 = mid.next
        mid.next = None
        head = mergeSort(head)
        h2 = mergeSort(h2)
        h1 = merge(head, h2)
        return h1





user_input = input()

list0 = [int(e) for e in user_input.split(" ")]
head = createLL(list0[:-1])
head = mergeSort(head)
printLL(head)

