class LinkedStack:
    def __init__(self):
        self.top = None
    def push(self, data):
        node = Node(data)
        if self.top == None:
            self.top = node
            return
        oldtop = self.top
        self.top = node
        self.top.next = oldtop
    def pop(self):
        if self.top == None:
            return
        if self.top.next == None:
            self.top = None
            return
        toBeTop = self.top.next
        del self.top
        self.top = toBeTop

    def peek(self):
        return self.top.data

    def printStack(self):
        print("\n")
        node = self.top
        while node != None:
            print(node.data)
            node = node.next

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

ll = LinkedStack()
ll.push(19)
ll.push(20)
ll.push(211)
ll.push(555)
ll.printStack()
ll.pop()
ll.printStack()


