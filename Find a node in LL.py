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
def find(head, i, data):
    if head is None:
        return -1
    if head.data == data:
        return i
    else:
        i += 1
        return find(head.next, i, data)






user_input = input()
data = int(input())
list0 = [int(e) for e in user_input.split(" ")]
head = createLL(list0[:-1])
i = 0
print(find(head, i, data))


