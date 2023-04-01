class Node:
    def __init__(self,datval=None):
        self.datval = datval
        self.nextval = None
class SLinkedList:
    def __init__(self):
        self.headval=None
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.datval)
            print(printval.nextval)
            printval = printval.nextval

    #insertion at the begining
    def AtBeginning(self,newdata):
        NewNode=Node(newdata)
        NewNode.nextval = self.headval
        self.headval=NewNode

    #insertion at the end
    def Atend(self,newdata):
        NewNode=Node(newdata)
        if self.headval is None:
            self.headval=NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste=laste.nextval
        laste.nextval = NewNode

    #Functon to add node
    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return
        NewNode = Node(newdata)
        NewNode.newxtval = middle_node.nextval
        middle_node.nextval = NewNode

    #print the linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print( printval.datval)
            printval=printval.nextval
    def delete_element_by_value(self,x):
        if self
list= SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
list.headval.nextval = e2
e2.nextval = e3
list.AtBeginning("Sun")
list.Atend("Thu")
list.listprint()
