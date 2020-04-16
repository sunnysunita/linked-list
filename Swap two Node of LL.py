"""class Node:
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


def swap(head):
    tail = head
    for i in range(1, m):
        tail = tail.next
    first = tail.next
    tail2 = head
    for j in range(1, n):
        tail2 = tail2.next
    prev = tail2
    second = tail2.next
    tail2 = second.next
    second.next = None
    if first == prev:
        second.next = first
        first.next = None
    else:
        second.next = first.next
        prev.next = first
        first.next = None
    tail.next = second
    first.next = tail2
    return head

user_input0 = input()
user_input1 = input()
list0 = [int(e) for e in user_input0.split(" ")]
list1 =[int(e) for e in user_input1.split(" ")]
m = list1[0]
n = list1[1]
head = createLL(list0[:-1])
head = swap(head)
printLL(head)
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def createLL(list):
    if len(list) == 0:
        return None
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

def swap_m_zero_n_one(head, m, n):
    if head is None:
        return
    c1 = head
    c2 = head.next
    a2 = c2.next
    c2.next = c1
    c1.next = a2
    return c2

def swapZero(head, m, n):
    if head is None:
        return
    c1 = head
    a1 = head.next
    p2 = head
    c2 = p2
    # for i in range(0, m-1):
    #     p1 = p1.next
    # c1 = p1.next
    # print("P1: ", p1.data)
    # print("C1: ", c1.data)

    for j in range(0, n-1):
        p2 = p2.next
    c2 = p2.next
    # print("P2: ", p2.data)
    # print("C2: ", c2.data)
    p2.next = c1
    c1.next = c2.next
    c2.next = a1
    return c2

def swap(head, m, n):

    p1 = head
    c1 = p1
    p2 = head
    c2 = p2
    for i in range(0, m-1):
        p1 = p1.next
    c1 = p1.next
    # print("P1: ", p1.data)
    # print("C1: ", c1.data)

    for j in range(0, n-1):
        p2 = p2.next
    c2 = p2.next
    # print("P2: ", p2.data)
    # print("C2: ", c2.data)

    p1.next = c2
    p2.next = c1
    c1.next = c2.next
    c2.next = p2
    return head

list0 = [int(e) for e in input().split(" ")]
list1 =[int(e) for e in input().split(" ")]
# print(list1)

head = createLL(list0[:-1])
if head is None:
    exit()

m = list1[0]
n = list1[1]
if m > n:
    m, n = n, m

if m == 0:
    if n == 1:
        printLL(swap_m_zero_n_one(head, m, n))
    else:
        printLL(swapZero(head, m, n))
else:
    printLL(swap(head, m, n))
