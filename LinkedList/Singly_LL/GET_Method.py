# WAP to find the element at a specific index element in a Singly Linked List

# Time Complexity = O(n)
# Space Complexity = O(1)


# The GET method rerturns the Node and we can return it's value as well
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

    def GET(self, index):
        if index == -1:
            return self.tail
        if index < -1 or index > self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
            # return index
        return current

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
print(new_list.GET(-1))
