# def fib(n):
#     a=0
#     b=1
#     if (n>=0):
#         print(a,end=" ")
#     if (n>=1):
#         print(b,end=' ')
#     for i in range(2,n+1):
#         c=a+b
#         print(c,end=" ")
#         a=b
#         b=c
# fib(4)

# def pivott(array,start,end):
#     pivot=array[start]
#     i=start+1
#     j=end
    
#     while True:
#         while i<=j and array[j]>=pivot:
#             j-=1
#         while i<=j and array[i]<=pivot:
#             i+=1
#         if i<=j:
#             array[i],[j]=array[j],[i]
#         else:
#             break
#     array[start],[j]=array[j],[start]
#     return j
# def quick_sort(array,start,end):
#     if start>=end:
#         return
#     p=pivott(array,start,end)
#     quick_sort=(array,p+1,end)
#     quick_sort(array,start,p-1)

# array=[2,7,0,4,7,3]
# quick_sort(array,0,len(array)-1)
# print(array)