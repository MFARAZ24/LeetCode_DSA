class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
        

    def get(self, index: int) -> int:
        if index<0 or index>=self.size:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        #self.size-=1
        return curr.val
        

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.size+=1
        
        
        

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        if self.head == None:
            self.head = newNode
        else:
            cur = self.head
            while cur.next!=None:
                cur = cur.next
            cur.next = newNode
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
            for _ in range(index-1):
                curr = curr.next
            newNode.next = curr.next
            curr.next = newNode
            self.size+=1

    

    def deleteAtIndex(self, index: int) -> None:
        
        if index<0 or index>=self.size:
            return
        elif index == 0:
            self.head = self.head.next
        elif index == self.size-1:
            curr = self.head
            while curr.next.next is not None:
                curr = curr.next
            curr.next = None
        
        else:
            curr = self.head
            for _ in range(index-1):
                curr = curr.next
            curr.next = curr.next.next
        self.size-=1

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)