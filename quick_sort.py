# import time
# start = time.perf_counter()

# def pivot(array,start,end):
#     pivot = array [start]
#     i = start+1
#     j = end

#     while(True):
#         while i <= j and array[j] >= pivot:
#             j-=1
#         while i <= j and array[i] <= pivot:
#             i+=1
#         if i <= j:
#             array[i],array[j] = array[j],array[i]
#         else:
#             break
#     array[start],array[j] = array[j],array[start]
#     return j 

# def QS(array,start,end):
#     if start >= end:
#         return
#     p=pivot(array,start,end)
#     QS(array,start,p-1)
#     QS(array,p+1,end)

# array = [3,1,4,2,6,7,9,8,5]
# QS(array,0,len(array)-1)
# print(array)

# end = time.perf_counter()
# print("time taken =",end-start)

import matplotlib.pyplot as plt
import numpy as np

x = [6,5,7,9]
y = [4.61,0.00,2.30,5.37]

plt.plot(x,y)
plt.xlabel('x axis ("No of input")')
plt.ylabel('y axis ("time")')
plt.title("Quick sort")
plt.savefig("output.png")

