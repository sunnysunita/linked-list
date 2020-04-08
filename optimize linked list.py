class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# we need to create a linked list which take input from user and return head node

def take_input():
    user_input = input("enter list of number separated by spaces: ")
    list_num = [int(e) for e in user_input.split(" ")]
    head = None
    tail = None
    for e in list_num:
        if e == -1:
            break
        new_node = Node(e)
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node
    return head

def printLL(head):
    while head is not None:
        print(str(head.data)+"->", end="")
        head = head.next
    print("None")
    return
head = take_input()
printLL(head)
