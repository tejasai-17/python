import time

start=time.perf_counter()
def search(arr, n, x):
    for i in range(0, n):
        if (arr[i] == x):
            return i
    return -1


arr = [2, 3,1,4,10]
x = 10
n = len(arr)

# Function call
result = search(arr, n, x)
if (result == -1):
    print("Element is not present in array")
else:
    print("Element is present at index", result)
end=time.perf_counter()
print("the time is:",end-start)