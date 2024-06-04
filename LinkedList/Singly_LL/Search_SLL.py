# WAP to find the specific element in a Singly Linked List

# Time Complexity = O(n)
# Space Complexity = O(1)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLL:
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

    def prepend(self, data):
        new_node = Node(data)
        temp = self.head

        if temp is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert(self, index, data):
        new_node = Node(data)
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

        self.length += 1

    def Traversal(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def SearchItem(self, target):
        current = self.head
        index = 0
        while current is not None:
            if current.data == target:
                return index
            current = current.next
            index += 1
        return "-1"

    def __str__(self):
        temp = self.head
        res = ""
        while temp is not None:
            res += str(temp.data)
            if temp.next is not None:
                res += "-> "
            temp = temp.next

        return res


new_list = SinglyLL()

new_list.append(11)
new_list.append(12)
new_list.append(13)
new_list.append(14)
print(new_list)

search1 = new_list.SearchItem(11)
search = new_list.SearchItem(19)
print(search1)
print(search)
