class Speaker:
    def invite_talk(self):
        pass

    def give_talk(self):
        pass


class Employee:
    def __init__(self, first_name, last_name, salary):
        self.id_num: int
        self.first_name = first_name
        self.last_name = last_name
        self._salary = salary
        self.benefits = 1000

    @property
    def salary(self):
        return self._salary

    def set_salary(self, salary):
        self._salary = salary


class PublicEmployee(Employee, Speaker):
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name, salary)


class Employees:
    def __init__(self):
        self.employees_dict = {}
        self.index = 101

    def add_employee(self, employee):
        employee.id_num = self.index
        self.index += 1
        self.employees_dict.update({employee.id_num: employee})

    def find(self, id_num):
        return self.employees_dict.get(id_num)


class TempEmployee(Employee):
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name, salary)
        self.benefits = 0


class Intern(TempEmployee):
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name, salary)
        self.set_salary(salary)

    def set_salary(self, salary):
        if salary > 500:
            self._salary = 500
        else:
            self._salary = salary


class HR:
    def __init__(self):
        self.employee_data = Employees()
        self.employee_data.add_employee(Employee('Sarah', 'Smythe', 2000))
        self.employee_data.add_employee(PublicEmployee('Fran', 'Alien', 3000))
        self.employee_data.add_employee(TempEmployee('Billy', 'Bob', 1000))
        self.employee_data.add_employee(Intern('Arnold', 'Stang', 800))

    def list_employees(self):
        employee_dict = self.employee_data.employees_dict
        for key in employee_dict:
            employee: Employee = employee_dict[key]
            print(employee.first_name, employee.last_name, employee.salary)


def main():
    hr = HR()
    hr.list_employees()


if __name__ == '__main__':
    main()
