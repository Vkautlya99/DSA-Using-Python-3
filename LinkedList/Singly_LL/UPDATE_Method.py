# WAP of UPDATE Method in a Singly Linked List

# Time Complexity = O(n)
# Space Complexity = O(1)


# UPDATE Method is Used to Update The value in a SLL and it uses two parameters (index , value/data)
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

    def UPDATE(self, index, data):
        temp = self.GET(index)
        if temp is not None:
            temp.data = data
            return True
        return False

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
# print(new_list.GET(-1))
print(new_list.UPDATE(0, 10))
print(new_list)
print(new_list.UPDATE(1, 20))
print(new_list)
