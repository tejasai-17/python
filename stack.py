class stack:
    def __init__(self,maxsize,top):
        self.maxsize=maxsize
        self.top=top
        self.list=[]

    def __str__(self):
        value = self.list.reverse()
        value = [str(x) for x in self.list]
        return '\n'.join (value)
    
    def push(self,value):
        if self.top==self.maxsize:
            print("the stack is full")
        else:
            self.list.append(value)
            self.top+=1
            print(value,"has successfully added")

    def pop(self):
        if self.top == -1:
            print("the stack is empty")
        else:
            print("popped item: ", self.list.pop())
            self.top-=1

    def display(self):
        if self.top == -1:
            print("the stack is empty")
        else:
            print("the stack is: ")
            print(self)

S=stack(5,-1)
S.push(10)
S.push(20)
S.push(30)
S.display()
S.pop()
S.display()