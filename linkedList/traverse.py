    
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    

def linked_list(head):
    
    current = head
    while current is not None:
        
        
        print(current.data)
              
        current = current.next
        
    print()

        
# head = Node(10)
# head.next = Node(20)
# head.next.next = Node(30)
# head.next.next.next = Node(40)

# print(head)