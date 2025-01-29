# print("hello world")
# print("i am Tejasai")
import time
start=time.perf_counter()
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = quick_sort(arr)
print("Quick Sorted array:", sorted_arr)
end=time.perf_counter()
print()
print("time=",end-start)
