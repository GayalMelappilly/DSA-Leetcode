class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next 

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return 
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data,None)


    def insert_values(self,values):
        self.head = None

        for value in values:
            self.insert_at_end(value)

    def remove_at(self,index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.head = self.head.next
            return 
        
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
            if count == index - 1:
                itr.next = itr.next.next
                break 

    def insert_at(self,index,data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.insert_at_beginning(data)

        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

            if count == index - 1:
                node = Node(data,itr.next)
                itr.next = node
                break
    
    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return 
        
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head

        while itr:
            count += 1
            itr = itr.next
        print(count)
        return count




if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(6)
    ll.insert_at_end(7)
    ll.print()
    ll.insert_values([1,2,3,4,5])
    ll.print()
    ll.get_length()
    ll.remove_at(2)
    ll.print()
    ll.insert_at(2,3)
    ll.print()

