import time

start = time.perf_counter()

open_list = ["[", "{", "("]  
close_list = ["]", "}", ")"]  

def checkP(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if (len(stack) > 0) and (open_list[pos] == stack[len(stack) - 1]):
                stack.pop()
        else:
            return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"


string = "{[()]}"
print(string, "-", checkP(string))
string = "{[()]}("
print(string, "-", checkP(string))
string = "((()))"
print(string, "-", checkP(string))

end = time.perf_counter()
print("time taken =", end-start)