class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    def insertAtBeginning(self, val):
        temp = self.head
        self.head = Node(val)
        self.head.next = temp
        self.size += 1
    def deleteAtBeginning(self):
        if self.head is not None:
            self.head = self.head.next
            self.size -= 1
    def insertAtEnd(self, val):
        if self.head is None:
            self.head = Node(val)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(val)
        self.size += 1
    def deleteAtEnd(self):
        if self.head is not None:
            if self.head.next is None:
                self.head = None
            else:
                cur = self.head
                while cur.next.next is not None:
                    cur = cur.next
                cur.next = None
            self.size -= 1
    def search(self, val):
        i = 0
        cur = self.head
        while cur is not None:
            if cur.val==val:
                return i
            cur = cur.next
            i += 1
        return "Value not present in list"
    def atIndex(self, val):
        if val<0 or val>=self.size:
            return "Not a valid index"
        i = 0
        cur = self.head
        while i<val:
            cur = cur.next
            i += 1
        return cur.val
    def print(self):
        if self.head is None:
            print('None')
        else:
            cur = self.head
            while cur is not None:
                print(cur.val, end='->')
                cur = cur.next
            print('None')
