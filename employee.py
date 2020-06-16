class Employee:
    _numberOfEmployees=0


    def __init__(self, name, family, salary, department):
        self._name=name
        self._family=family
        self._salary=salary
        self._department=department

        Employee._numberOfEmployees+=1


    def getName(self):
        return self._name
    def getFamily(self):
        return self._family
    def getSalary(self):
        return self._salary
    def getDepartment(self):
        return self._department

    def average_Salary(self,employees:list) -> int :
        total=0
        for employee in employees:
            total += employee.getSalary()
        return total


class FullTimeEmployee(Employee):
    def __init__(self,name, family, salary, department,hours):
        super.__init__(name, family, salary, department)
        self.numberofhours=hours



a=Employee("Nika",'Dzidzava',100000,'CS')
b=Employee("Nika",'Dzidzava',100000,'CS')

print(a.getName(), b.getFamily())