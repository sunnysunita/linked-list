class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

list = [1, 2, 3, 4, 5, 6, -1]

def insertLL(head, i, data):

    len = countLL(head)
    if i > len or i < 0:
        return head
    else:
        newNode = Node(data)
        prev = None
        after = head
        if i == 0:
            head = newNode
            head.next = after
            return head
        else:
            for i in range(0, i):
                prev = after
                after = after.next
            prev.next = newNode
            newNode.next = after
            return head
def countLL(head):
    count=0
    while head is not None:
        count += 1
        head = head.next
    return count

def createLL(list):
    head = Node(list[0])
    tail = head
    for e in list[1:]:
        newNode = Node(e)
        tail.next =newNode
        tail = newNode
    return head

def printLL(head):
    while head is not None:
        print(str(head.data)+"->",end="")
        head = head.next
    print("None")


head = createLL(list[:-1])
printLL(head)
head = insertLL(head, 0, 7)
printLL(head)
print(countLL(head))
print(head.data)