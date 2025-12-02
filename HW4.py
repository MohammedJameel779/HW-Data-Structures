class Node:
    def __init__(self , data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_head(self , data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def insert_at_tail(self , data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head 
        while temp.next:
            temp = temp.next
            temp.next = new_node
            
            #
    def search (self , target):
        temp = self.head
        while temp:
            if temp.data == target:
                return True
            temp = temp.next
            return False
    
    def delete ( self , target):
        if not self.head:
            return
        
        #
        if self.head.data == target:
            self.head = self.head.next
            return
        
        temp = self.head
        while temp.next:
            if temp.next.data == target:
                temp.next = temp.next.next
                return
            temp = temp.next
            
    def print_list (self):
        temp = self.head
        while temp:
            print(temp.data , end =" ->")
            temp = temp.next
            print("None")
            
    def count_nodes(self):
        count = 0
        temp = self.head
        while temp:
            count +=1
            temp = temp.next
            return count
        
ll = LinkedList()

ll.insert_at_head(10)
ll.insert_at_tail(20)
ll.insert_at_tail(30)
ll.insert_at_head(5)

ll.print_list()

print ( "Is there 20 ?",ll.search(20))
print ( "Number of nodes = ",ll.count_nodes())

ll.delete(20)
print ("After Deletion")
ll.print_list()