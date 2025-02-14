# print("hello world")
# print("i am Tejasai")
# import time
# start=time.perf_counter()
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quick_sort(left) + middle + quick_sort(right)

# arr = [64, 34, 25, 12, 22, 11, 90]
# sorted_arr = quick_sort(arr)
# print("Quick Sorted array:", sorted_arr)
# end=time.perf_counter()
# print()
# print("time=",end-start)               

# def privote(array,start,end):
#     pivot=array[start]
#     i=start+1
#     j=end

#     while True:
#         while i<=j and array[j] >= pivot:def fib(n):

# def fib(n):
#     a=1
#     b=1
#     if(n>=0):
#         print(a,end=' ')
#     if(n>=1):
#         print(b,end=' ')
#     for i in range(2,n+1):
#         c=a+b
#         print(c,end=' ')
#         a=b
#         b=c
# fib(8)
        
#             i+=1
#         if i<=j:
#             array[i],array[j]=array[j],array[i]
#         else:
#             break
#     array[start],array[j]=array[j],array[start]
#     return j

# def quick_sort(array,start,end):
#     if start >= end:
#         return
    
#     p=privote(array,start,end)
#     quick_sort(array,p+1,end)
#     quick_sort(array,start,p-1)

# array=[6,3,5,9,8,7,2]
# quick_sort(array,0,len(array) -1)
# print(array)

# def fib(n):
#     a=0
#     b=1
#     if n>=0:
#         print(a,end=" ")
#     if n>=1:
#         print(b,end=" ")
#     for i in range (2,n+1):
#         c=a+b
#         print(c,end=" ")
#         a=b
#         b=c
# fib(8)        


# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next

# class LinkedList:

#     def __init__(self):
#         self.head = None

#     def insert(self, data):
#         new_node = Node(data)
#         if (self.head):
#             current = self.head
#             while (current.next):
#                 current = current.next
#             current.next = new_node
#         else:
#            self.head = new_node

#     def print_iter(self):
#         current_item = self.head
#         while current_item:
#             val = current_item.data
#             current_item = current_item.next
#             yield val

# LL = LinkedList()
# LL.insert(1)
# LL.insert(2)
# LL.insert(3)
# LL.insert('welcome')
# LL.insert('python')

# for item in LL.print_iter():
#     print(item)

# import time
# start=time.perf_counter()
# def bubbleSort(arr):
#    n = len(arr)
#    for  i in range(n-1):
#        for j in range(0, n-i-1):
#            if arr[j] >arr[j + 1] :
#                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# arr = [64, 34, 25, 12, 22, 11, 90]

# bubbleSort(arr)

# print ("Sorted array is:")
# for i in range(len(arr)):
#     print ("% d" % arr[i],end=" ")
    
# end=time.perf_counter()
# print()
# print("time=",end-start)

# import time
# start=time.perf_counter()
# def selectionSort(array):
#     n = len(array)
#     for i in range(n):
#         minimum = i

#         for j in range(i + 1, n):
#             if (array[j] < array[minimum]):
#                 minimum = j

#         temp = array[i]
#         array[i] = array[minimum]
#         array[minimum] = temp

#     return array

# array = [13, 4, 9,45,12]
# print("sortedlist =",selectionSort(array))
# end=time.perf_counter()
# print("the time is:",end-start)

# import time
# start=time.perf_counter()

# def insertionSort(array):
#     for i in range(1, len(array)):
#         key = array[i]
#         j = i - 1

#         while j >= 0 and key < array[j]:
#             array[j + 1] = array[j]
#             j = j - 1

#         # Place key at after the element just smaller than it.
#         array[j + 1] = key

# arr = [9, 5, 1, 4, 3]
# insertionSort(arr)
# print('Sorted Array in Ascending Order:',arr)
# end=time.perf_counter()
# print("the time is:",end-start)

# def binarySearch(array, x, low, high):
#     if low<= high:
#         mid = low + (high - low)//2
#         if array[mid]== x:
#             return mid
#         elif array[mid] > x:
#             return binarySearch(array, x, low, mid-1)
#         else:
#             return binarySearch(array, x, mid + 1, high)
#     else:
#         return -1

# array = [3, 4, 5, 6, 7, 8, 9]
# x = 7
# result = binarySearch(array, x, 0, len(array)-1)
# if result != -1:
#     print("Element is present at index: " + str(result))
# else:
#     print("Not found")

# def   mergeSort(myList):
#     if len(myList) > 1:
#         mid = len(myList) // 2
#         left = myList[:mid]
#         right = myList[mid:]
#         mergeSort(left)
#         mergeSort(right)
#         i = 0
#         j = 0
#         k = 0
#         while i < len(left) and j < len(right):
#             if left[i] <= right[j]:
#                    myList[k] = left[i]
#                    i += 1
#             else:
#                 myList[k] = right[j]
#                 j += 1
#             k += 1
#         while i < len(left):
#             myList[k] = left[i]
#             i += 1
#             k += 1
#         while j < len(right):
#             myList[k]=right[j]
#             j += 1
#             k += 1

# myList = [54,26,93,17,77,31,44,55,20]
# mergeSort(myList)
# print(myList) 

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class LinkedList:

#     def __init__(self):
#         self.head = None

#     def insertAtBeginning(self, new_data):
#         new_node = Node(new_data)
#         new_node.next = self.head
#         self.head = new_node

#     def delete_beginning(self):
#         if self.head is None:
#             print("Linked list is empty. Cannot delete the elements")
#         else:
#             self.head = self.head.next

#     def search(self, key):

#         current = self.head

#         while current is not None:
#             if current.data == key:
#                 return True

#             current = current.next

#         return False

#     def printList(self):
#         temp = self.head
#         while (temp):
#             print(str(temp.data) + " ", end="")
#             temp = temp.next


# if __name__ == '__main__':

#     llist = LinkedList()
#     llist = LinkedList()
#     n=Node(1)
#     llist.head=n
#     n1=Node(2)
#     n.next=n1
    
#     llist.insertAtBeginning(10)
#     llist.insertAtBeginning(20)
#     llist.insertAtBeginning(30)
#     llist.insertAtBeginning(40)
#     llist.insertAtBeginning(50)
#     print('linked list:')
#     llist.printList()

#     print("\nAfter deleting an element:")
#     llist.delete_beginning()
#     llist.printList()

#     print()
#     item_to_find = 10
#     if llist.search(item_to_find):
#         print(str(item_to_find) + " is found")
#     else:
#         print(str(item_to_find) + " is not found")
    
#     print("linked list is")
#     llist.printList()

