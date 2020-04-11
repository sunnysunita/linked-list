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


def palindrome(head, count):
    if count == 1 or count == 0:
        return True
    if count == 2:
        if head.data == head.next.data:
            return True
        else:
            return False
    if count == 3:
        if head.data == head.next.next.data:
            return True
        else:
            return False
    if count % 2 == 0:
        i = count // 2
        tail = head
        for e in range(1, i):
            tail = tail.next
        head2 = tail.next
        tail.next = None
        head2 = reverseLL(head2)
        # print("second part of LL")
        # printLL(head2)
        # print("first part of LL")
        # printLL(head)
        for e in range(1, i):
            if head.data != head2.data:
                return False
            head = head.next
            head2 = head2.next
        return True
    else:
        i = count // 2
        tail = head
        for e in range(1, i):
            tail = tail.next
        head2 = tail.next.next
        tail.next = None
        head2 = reverseLL(head2)
        # print("second part of LL")
        # printLL(head2)
        # print("first part of LL")
        # printLL(head)
        for e in range(1, i):
            if head.data != head2.data:
                return False
            head = head.next
            head2 = head2.next
        return True


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


def merge1(h1, h2):
    head = Node(-1)
    tail = head
    while h1 is not None and h2 is not None:
        if h1.data < h2.data:
            newNode = Node(h1.data)
            tail.next = newNode
            tail = newNode
            # print(tail.data,end=" ")
            newNode = Node(h2.data)
            tail.next = newNode
            tail = newNode
            # print(tail.data,end=" ")
        else:
            newNode = Node(h2.data)
            tail.next = newNode
            tail = newNode
            # print(tail.data,end=" ")
            newNode = Node(h1.data)
            tail.next = newNode
            tail = newNode
            # print(tail.data,end=" ")
        h1 = h1.next
        h2 = h2.next

    while h1 is not None:
        newNode = Node(h1.data)
        tail.next = newNode
        tail = newNode
        # print(tail.data,end=" ")
        h1 = h1.next
    while h2 is not None:
        newNode = Node(h2.data)
        tail.next = newNode
        tail = newNode
        # print(tail.data,end=" ")
        h2 = h2.next

    tail.next = None

    return head.next


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


user_input0 = input()
user_input1 = input()
list0 = [int(e) for e in user_input0.split(" ")]
h1 = createLL(list0[:-1])

list1 = [int(e) for e in user_input1.split(" ")]
h2 = createLL(list1[:-1])

head = merge(h1, h2)

printLL(head)
