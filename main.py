class LinkedStack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        #we check if there is no data in the stack..
        if self.top == None:
            self.top = node
            return
        #we need to store current top value
        oldtop = self.top
        #we push our new node into top...
        self.top = node
        #we link the new top node to old one...
        self.top.next = oldtop

    def pop(self):
        #if there is no data we return.
        if self.top == None:
            return
        #if we have just 1 item in the stack, we just assign None
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

currentTop = ll.peek()
print("Current Top Data is..." + str(currentTop))


