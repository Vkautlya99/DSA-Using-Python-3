# Creation Of Node Class


# Method :- 1
class MyNode:
    def __init__(self, value):
        self.value = value
        self.next = None


My_Node = MyNode(1)
print(My_Node)


# Method :- 2
class Node:
    def __init__(self, Data=None, Next=None):
        self.Data = 0
        self.Next = 0


new_Node = Node(2)
print(new_Node)
