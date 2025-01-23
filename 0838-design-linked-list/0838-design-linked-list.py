class ListNode:
    def __init__(self, val = 0):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        

    def get(self, index: int) -> int:
        if index<0 or index>=self.size:
            return -1
        curr = self.head
        for _ in range(index+1):
            curr = curr.next
        #self.size-=1
        return curr.val
        

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.prev = self.head
        newNode.next = self.head.next
        self.head.next.prev = newNode
        self.head.next = newNode
        self.size+=1
        

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.tail
        newNode.prev = self.tail.prev
        self.tail.prev.next = newNode
        self.tail.prev = newNode
        self.size+=1

    def addAtIndex(self, index: int, val: int) -> None:
        if index<0 or index>self.size:
            return
        elif index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)

        else:
            newNode = ListNode(val)
            curr = self.head
            for _ in range(index):
                curr = curr.next
            newNode.prev = curr
            newNode.next = curr.next
            curr.next.prev = newNode
            curr.next = newNode
            self.size+=1

        

    def deleteAtIndex(self, index: int) -> None:
        if index>=self.size or index<0:
            return
        elif index == 0:
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
        elif index == self.size-1:
            self.tail.prev = self.tail.prev.prev
            self.tail.prev.next = self.tail

        else:
            curr = self.head
            for _ in range(index):
                curr = curr.next
            curr.next = curr.next.next
            curr.next.prev = curr
        self.size-=1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)