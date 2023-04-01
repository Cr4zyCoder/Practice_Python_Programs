# write a python program function which accepts two linked lists containing integer data and an integer, n and merges
# the two linked lists, such that list2 is merged with list1 after n number of nodes. Assume that value of n will always
# be less than or equal to thr number of nodes in list1. ?

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

def merge_lists_after_n_nodes(list1, list2, n):
    current = list1.head
    for i in range(n-1):
        current = current.next
    temp = current.next
    current.next = list2.head
    current = current.next
    while current.next:
        current = current.next
    current.next = temp

# Example Usage
list1 = LinkedList()
list1.add_node(1)
list1.add_node(2)
list1.add_node(3)
list1.add_node(4)
list1.add_node(5)

list2 = LinkedList()
list2.add_node(6)
list2.add_node(7)
list2.add_node(8)

merge_lists_after_n_nodes(list1, list2, 3)
list1.print_list()  
