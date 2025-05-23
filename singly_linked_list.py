import time
start = time.perf_counter()
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Deleting a node
    def delete_beginning(self):
        if self.head is None:
            print("Linked list is empty. Cannot delete the elements")
        else:
            self.head = self.head.next

    # Search an element
    def search(self, key):

        current = self.head

        while current is not None:
            if current.data == key:
                return True

            current = current.next

        return False

    # Print the linked list
    def printList(self):
        temp = self.head
        while (temp):
            print(str(temp.data) + " ", end="")
            temp = temp.next


if __name__ == '__main__':

    llist = LinkedList()
    llist = LinkedList()
    n=Node(1)
    llist.head=n
    n1=Node(2)
    n.next=n1
    
    llist.insertAtBeginning(10)
    llist.insertAtBeginning(20)
    llist.insertAtBeginning(30)
    llist.insertAtBeginning(40)
    llist.insertAtBeginning(50)
    print('linked list:')
    llist.printList()

    print("\nAfter deleting an element:")
    llist.delete_beginning()
    llist.printList()

    print()
    item_to_find = 10
    if llist.search(item_to_find):
        print(str(item_to_find) + " is found")
    else:
        print(str(item_to_find) + " is not found")
    
    print("linked list is")
    llist.printList()

end = time.perf_counter()
print("time taken: ",end-start)

