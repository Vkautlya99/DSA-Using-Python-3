# Delete an Element from The last Of A Linked List
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

    def pop(self):
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.next = temp
            temp.next = None
            self.length -= 1
            return popped_node

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
new_Linked_List.append(10)
new_Linked_List.append(20)
new_Linked_List.append(30)
print(new_Linked_List)
new_Linked_List.pop()
print(new_Linked_List)
