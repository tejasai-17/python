import  emp
import time
start=time.perf_counter()
def main():
    emp1 = emp.Employee ('name', 'id', 'department')
    emp2 = emp.Employee ('name', 'id', 'department')
    emp3 = emp.Employee ('name', 'id', 'department')
    emp1.set_name('Suma')
    emp1.set_id('47899')
    emp1.set_department('Accounting')
    print(emp1)
main()
end=time.perf_counter()
print()
print("time=",end-start)
