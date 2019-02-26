from mylistiterator import MyListIterator
class Mylist:

       def __init__(self):
               self.head = None

       def insert(self,data):
               data = input("Add an element:")
               node = Node()
               node.data = data
               node.next = self.head
               self.head = node

       def print(self):
               print_list = self.head
               while print_list:
                       print(print_list.data)
                       print_list = print_list.next

       def size(self):
               i=0
               head = self.head
               while head:
                      i+=1
                      head = head.next
               print (i)
