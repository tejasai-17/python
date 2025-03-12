graph = {'a':['b','d','e','f'],'d':['a'],'b':['a','f','c'],'f':['b','a'],'c':['b'],'e':['a']}
print ("Given Graph is:")
print(graph)

def dfs(input_graph,source):
    stack = list()
    visited_list = list()
    stack.append(source)
    visited_list.append(source)
    while stack:
        vertex = stack.pop()
        print(vertex, end=" ")
        for u in input_graph[vertex]:
            if u not in visited_list:
                stack.append(u)
                visited_list.append(u)

print("DFS traversal of graph with source A is: ")
dfs(graph, "a")


