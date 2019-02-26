from myclass import travell 
from linked_list import Mylist
from linked_class import Queue

 
def __init__(self,country,city,month):
 travell1 = travell()   
 country = "italy" 
 city = "rome"
 month = "june"
 travell1.change_inf(country, city, month)
 
 
def __init__(self,country,city,month):
 travell2 = travell()
 country = "Kazakhstan" 
 city = "Taraz"
 month = "march"
 travell2.change_inf(country, city, month) 
def __init__(self,country,city,month):
 travell3 = travell()
 country = "Japan" 
 city = "Tokyo"
 month = "august"
 travell3.change_inf(country, city, month) 



my_Queue = Queue()
my_Queue(travell1)
my_Queue(travell2)
my_Queue(travell3)


print(my_Queue.length())
my_Queue.dequeue().disp_inf()
print(my_Queue.length())
my_Queue.dequeue().disp_inf()

