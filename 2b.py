import time
start = time.perf_counter()
class Employee:
    def GetEmployeeInfo(self):
        self.__rollno = input("Enter Roll Number: ")
        self.__name = input("Enter Name: ")
        self.__department = input("Enter the department: ")

    def printResult(self):
        print(self.__rollno,self.__name,self.__department)

EmpArray = []

while(True):
    emp = Employee()
    emp.GetEmployeeInfo()
    EmpArray.append(emp)
    ch = input("Add More y/n?: ")
    if(ch=='n'):break

print("Employee details are: ")

for emp in EmpArray:
    emp.printResult()

end = time.perf_counter()
print()

print("time=", end - start)