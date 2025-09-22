# singly linked list 


class singlyNode:
    
    def __init__(self, value, next=None):
        self.value = value
        self.next = next 

    def __str__(self):
        return str(self.value)
    


# Now we have to set data and makes the connection

Head = singlyNode(120)
A = singlyNode(420)
B = singlyNode(100)
C = singlyNode(500)

# Now for the connection 

Head.next = A
A.next = B
B.next =C

print(A)


curr = Head 
while curr:
    print(curr)
    curr = curr.next 

# Now for displaying linked list - O(n)
def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.value))
        curr = curr.next
    print('  -> '.join(elements))

display(Head)

# Searching for a node !