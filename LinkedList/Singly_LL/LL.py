# Create a LL That Contains Only One Node i.e :- Head & Tail


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# class LinkedList:
#     def __init__(self, data):
#         new_node = Node(data)
#         self.head = new_node
#         self.tail = new_node
        
#         self.length = 1
        # Empty LL


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        NewNode = Node(data)
        self.head = NewNode
        self.tail = NewNode
        self.length = 1 

My_Node = LinkedList()
My_Node.append(22)
print(My_Node)

print(My_Node.head.data)
print(My_Node.tail.data)
print(My_Node.length)

