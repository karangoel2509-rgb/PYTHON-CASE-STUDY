


class Employee:
    def __init__(self, emp_id, name, base_pay):
        self.__id = emp_id
        self.__name = name
        self.__base_pay = base_pay

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_base_pay(self):
        return self.__base_pay

    def get_hra(self):
        return self.__base_pay * 0.20

    def get_da(self):
        return self.__base_pay * 0.50

    def compute_gross(self):
        return self.__base_pay + self.get_hra() + self.get_da()

    def compute_tax(self):
        return self.compute_gross() * 0.10

    def compute_net(self):
        return self.compute_gross() - self.compute_tax()

    def print_salary_slip(self):
        print("****************************************")
        print(f"      SALARY SLIP: {self.__name.upper()}")
        print("****************************************")
        print(f"Employee ID : {self.__id}")
        print("----------------------------------------")
        print(f"Base Pay    : {self.__base_pay}")
        print(f"HRA         : {self.get_hra()}")
        print(f"DA          : {self.get_da()}")
        print("----------------------------------------")
        print(f"Gross Pay   : {self.compute_gross()}")
        print(f"Tax Deduct  : {self.compute_tax()}")
        print("****************************************")
        print(f"NET SALARY  : {self.compute_net()}")
        print("****************************************")

if __name__ == "__main__":
    e1 = Employee("EMP-842", "Aman Gupta", 55000)
    e2 = Employee("EMP-915", "Priya Singh", 72000)

    e1.print_salary_slip()
    print("\n")
    e2.print_salary_slip()