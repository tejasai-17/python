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
#         while i<=j and array[j] >= pivot:
#             j-=1
#         while i<=j and array[i] <= pivot:
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
