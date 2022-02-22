def insertAtEndInCLL (self, data):
     current = self. head
     newNode = Node()
     newNode.setData(data)
     while current.getNext != self.head:
           current = current.getNext()
     newNode. setNext(newNode)
     if self.head == None:
      self.head = newNode;
     else:
      newNode.setNexl(self.head)
      current.setNext(newNode)

def insertALBeginInCLL (self, data):
     current = self.head
     newNode = Node()
     newNode.setData(data)
     while current.getNext != self.head:
       current = current.getNext()
     newNode.setNext(newNode)
     if self.head == None:
         self.head = newNode;
     else:
      newNode.setNext(self. head)
      current.setNext(newNode)
      self.head = newNode

def deleteLastNodeFromCLL (self):
   temp = self.head
   current = self.head
   if self.head == None:
    print ("List Empty")
    return
   while current.getNext() != self.head:
     temp = current;
     current = current.getNextQ
   temp.sctNexl(current.getNext())
   return

def deleteFrontNodeFromCLL (self):
  current = self. head
  if self.head == None:
    print("List Empty")
    return
  while current.getNext() != self.head:
    current = current.gulNcxt()
  current.setNext(self. head.getNext())
  self.head = self.head.getNextQ
  return