class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# we need to create a linked list which take input from user and return head node

def take_input():
    user_input = input("enter list of number separated by spaces: ")
    list_num = [int(e) for e in user_input.split(" ")]
    head = None
    for e in list_num:
        if e == -1:
            break
        new_node = Node(e)
        if head is None:
            head = new_node
        else:
            curr=head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
    return head

def printLL(head):
    while head is not None:
        print(str(head.data)+"->", end="")
        head = head.next
    print("None")
    return
head = take_input()
printLL(head)













"""a = Node(10)
b = Node(20)
print(a.data)
print(b.data)
a.next = b  # referencing node a with b

print(a.next.data)
# print(b.next.data)
"""