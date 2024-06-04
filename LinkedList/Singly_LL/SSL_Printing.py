# Write a Programm to print the Nodes of a Singly Linked List in the Format of ( A-> B-> C-> ......)


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

    def __str__(self):
        temp = self.head
        res = ""

        while temp is not None:
            res += str(temp.data)
            if temp.next is not None:
                res += "-> "
            temp = temp.next
        return res


new_Linked_List = LinkedList()
new_Linked_List.append(22)
new_Linked_List.append(30)
new_Linked_List.append(40)
new_Linked_List.append(50)
print(new_Linked_List)
