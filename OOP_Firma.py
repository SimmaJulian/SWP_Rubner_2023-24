class Person:
    def __init__(self, firstname, lastname, age, is_male):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.is_male = is_male
        
    def __str__(self):
        is_male = "männlich" if self.is_male else "weiblich"
        return f"Vorname = {self.firstname}, Nachname = {self.lastname}, Alter = {self.age}, Ist_männlich = {is_male}"

class Employee(Person):
    def __init__(self, firstname, lastname, age, is_male, department):
        super().__init__(firstname, lastname, age, is_male)
        self.department = department
        
    def __str__(self):
        return super().__str__() + f", Abteilung = {self.department}"

class Department_Head(Employee):
    def __init__(self, firstname, lastname, age, is_male, department):
        super().__init__(firstname, lastname, age, is_male, department)
        
    def __str__(self):
        return super().__str__() + f", Abteilung = {self.department}"



class Company:
    def __init__(self, name, employees=None, departments=None, department_heads=None):
        self.name = name
        if employees is None:
            self.employees = []
        if departments is None:
            self.departments = []
        if department_heads is None:
            self.department_heads = []

  
    def add_employee(self, emp):
        if type(emp) is Employee:
            if emp.department in self.departments:
                self.employees.append(emp)
            else:
                print("Diese Abteilung existiert nicht!")
            
    def add_department_head(self, dep_head):
        if type(dep_head) is Department_Head:
            if dep_head.department in self.departments:
                if not any(dh.department == dep_head.department for dh in self.department_heads):
                    self.department_heads.append(dep_head)
                else:
                    print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("Es gibt bereits einen Abteilungsleiter für diese Abteilung")
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            else:
                print("Diese Abteilung existiert nicht")

                
    
    def add_department(self, dep):
        self.departments.append(dep)

    def remove_employee(self, emp):
        self.employees.remove(emp)

    def remove_department_head(self, dep_head):
        self.department_heads.remove(dep_head)

    def remove_department(self, dep):
        self.departments.remove(dep)
 
    
    def show_employees(self):
        print("\n########################################")
        print(f'Anzahl Mitarbeiter: {len(self.employees)} ')
        for employee in self.employees:
            print(f'{employee.lastname} {employee.firstname}')


    def show_departments(self):
        print("\n########################################")
        print(f'Anzahl Abteilungen: {len(self.departments)} ')
        for department in self.departments:
            print(f'{department}')

    def show_department_heads(self):
        print("\n########################################")
        print(f'Anzahl Abteilungsleiter: {len(self.department_heads)} ')
        for department_head in self.department_heads:
            print(f'{department_head.lastname} {department_head.firstname} -> {department_head.department}')

    def employees_per_department(self):
        print("\n########################################")
        dict = {k: 0 for k in self.departments}

        for i in self.employees:
            dict[i.department] += 1

        print(f'Mitarbeiter pro Abteilung:')
        for j in dict:
            print(f'{j}: {dict[j]}')


    def male_persentage(self):
        print("\n########################################")
        dict = {'male': 0, 'female': 0}
        for i in self.employees:
            dict['male' if i.is_male else 'female'] += 1
        for j in self.department_heads:
            dict['male' if j.is_male else 'female'] += 1

        
        print(f'Anzahl Männer = {dict["male"]}')
        print(f'Anzahl Frauen = {dict["female"]}')
        count_male = round(dict["male"] / (dict["male"] + dict["female"]) *100 ,2)
        print(f'Verhältniss = {count_male}% Männer und {100 - count_male}% Frauen')



        
        
        
    
def main():
    firma = Company("Testfirma")
    em1 = Employee("Luca", "Sepe", 10, False, "r&d")
    em2 = Employee("Mama", "Mark", 23, True, "finance")
    em3 = Department_Head("Max", "Strebl", 17, True, "production")
    em4 = Employee("Tim", "Timi", 7, True, "r&d")
    em5 = Department_Head("Lara", "Warte", 16, False, "r&d")
    em6 = Employee("Steff", "DerKeff", 21, True, "finance")
    em7 = Department_Head("saf", "aeva", 17, True, "production")
    
    firma.add_department('r&d')
    firma.add_department('finance')
    firma.add_department('production')
    
    firma.add_employee(em1)
    firma.add_employee(em2)
    firma.add_employee(em4)
    firma.add_employee(em6)

    firma.add_department_head(em3)    
    firma.add_department_head(em5)
    firma.add_department_head(em7)


    firma.show_department_heads()
    firma.show_employees()
    firma.show_departments()
    firma.male_persentage()
    firma.employees_per_department()

if __name__ == "__main__":
    main()

    