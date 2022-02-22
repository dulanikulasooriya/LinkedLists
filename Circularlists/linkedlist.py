def __init__(self):
        self.head = None
        self.length = 0

def Listlength(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            print(current.getData())
            current = current.getNext()
        return count

def addNodeBeginning(self, data):
        newNode = Node()
        newNode.setData(data)

        if self.head is None:
            self.head = newNode
        else:
            newNode.setNext(self.head)
            self.head = newNode
        self.length += 1


