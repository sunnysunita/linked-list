
def sortList(head):


    swap = 0
    if head != None:
        while(1):

            swap = 0
            tmp = head
            while(tmp.next != None):
                if tmp.val > tmp.next.val:
                    # swap them
                    swap += 1
                    p = tmp.val
                    tmp.val = tmp.next.val
                    tmp.next.val = p
                    tmp = tmp.next
                else:
                    tmp = tmp.next

            if swap == 0:
                break
            else:
                continue



        return head
    else:
        return head

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


def reverse(head, k):
    current = head
    next = None
    prev = None
    count = 0
    while(current is not None and count < k):
        next = current.next
        current.next = prev
        prev = current
        current = next
        count += 1
    if next is not None:
        head.next = reverse(next, k)

    return prev


list = [int(e) for e in input().split()]
k = int(input())
head = createLL(list[:-1])
head = sortList(head)
printLL(head)
