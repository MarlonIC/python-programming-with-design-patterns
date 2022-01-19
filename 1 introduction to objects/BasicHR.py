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


class Employees:
    def __init__(self):
        self.empty_dict = {}
        self.index = 101

    def add_employee(self, employee):
        employee.id_num = self.index
        self.index += 1
        self.empty_dict.update({employee.id_num: employee})

    def find(self, id_num):
        return self.empty_dict.get(id_num)


class HR:
    def __init__(self):
        self.empty_data = Employees()
        self.empty_data.add_employee(Employee('Sarah', 'Smythe', 2000))
        self.empty_data.add_employee(Employee('Billy', 'Bob', 1000))
        self.empty_data.add_employee(Employee('Edward', 'Elgar', 2200))

    def list_employees(self):
        dict_employees = self.empty_data.empty_dict
        for key in dict_employees:
            employee = dict_employees[key]
            print(employee.first_name, employee.last_name, employee.salary)


def main():
    hr = HR()
    hr.list_employees()
    fred = Employee('Fred', 'Smythe', 1200)


if __name__ == '__main__':
    main()
