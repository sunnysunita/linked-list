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

def deleteN(head):
    if m == 0:
        return None
    K = head
    D = K
    while K is not None or D is not None:
        for i in range(1, m):
            if K is None:
                return head
            K = K.next
        D = K.next
        K.next = None

        for j in range(0, n):
            if D is None:
                K.next = None
                return head
            D = D.next

        K.next = D
        K = D
    return head





user_input = input()
m = int(input())
n = int(input())
list0 = [int(e) for e in user_input.split(" ")]
head = createLL(list0[:-1])
head = deleteN(head)
printLL(head)
