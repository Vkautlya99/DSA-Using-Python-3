# Write a Programm to Insert the Node at last in a Singly Linked List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1


new_Linked_List = LinkedList()
new_Linked_List.append(22)
new_Linked_List.append(30)
# new_Linked_List.append(40)
# new_Linked_List.append(50)
# new_Linked_List.append(60)
print(new_Linked_List.head.data)
print(new_Linked_List.tail.data)
print(new_Linked_List.length)
