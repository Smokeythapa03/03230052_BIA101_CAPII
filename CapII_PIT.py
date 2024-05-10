class Taxpayer:
    def __init__(self, name, income):
        self.name = name
        self.income = income

    def calculate_total_deductions(self):
        # Default implementation returns 0 deductions
        return 0
    
class Income(Taxpayer):
    def __init__(self, monthly_salary):
        # Assuming monthly salary is provided
        self.monthly_salary = monthly_salary

    def calculate_annual_income(self):
        return self.monthly_salary * 12

class Employee(Taxpayer):
    def __init__(self, name, monthly_income, NPPF_deductions, children_allowance_per_child, number_of_children, GIS_deductions, health_insurance_deduction=1000, organization_type='Corporate', is_contract_employee=False):
        super().__init__(name, monthly_income * 12)  # Convert monthly income to annual income
        self.NPPF_deductions = NPPF_deductions
        self.children_allowance_per_child = children_allowance_per_child
        self.number_of_children = number_of_children
        self.GIS_deductions = GIS_deductions
        self.health_insurance_deduction = health_insurance_deduction
        self.organization_type = organization_type
        self.is_contract_employee = is_contract_employee

    def calculate_total_deductions(self):
        total_deductions = super().calculate_total_deductions()
        if not self.is_contract_employee:
            total_deductions += self.NPPF_deductions
        # Multiply children allowances by the number of children
        total_deductions += self.children_allowance_per_child * self.number_of_children
        total_deductions += self.GIS_deductions
        total_deductions += self.health_insurance_deduction  # Include health insurance deduction
        return total_deductions
    
    def calculate_tax(self):
        total_deductions = self.calculate_total_deductions()  # Call the method to get the total deductions
        taxable_income = self.income - total_deductions

        tax_bracket = [
            (300000, 0),
            (500000, 0.05),
            (800000, 0.10),
            (1200000, 0.15),
            (2000000, 0.20),
            (float('inf'), 0.25)
        ]

        total_tax = 0

        for threshold, tax_rate in tax_bracket:
            if taxable_income <= threshold:
                total_tax += taxable_income * tax_rate
                break

        return total_tax


if __name__ == '__main__':
    # Input for regular employees
    name = input('Enter employee name: ')
    monthly_income = float(input("Enter employee monthly income:"))
    is_contract_employee = input('Is the employee a contract employee? (y/n):').lower() == 'yes'
    NPPF_deductions = float(input('Enter NPPF deductions:'))
    children_allowance_per_child = float(input('Enter children allowances per child:'))
    number_of_children = int(input('Enter number of children:'))
    GIS_deductions = float(input('Enter GIS deductions:'))

    # Create employee instance based on user input
    employee = Employee(name, monthly_income, NPPF_deductions, children_allowance_per_child, number_of_children, GIS_deductions, is_contract_employee=is_contract_employee)

    # Calculate tax for the employees
    tax = employee.calculate_tax()

    # Display tax informations
    print(f"{employee.name} has an annual income of Nu.{employee.income:.2f}. After deductions, the taxable income is Nu.{employee.income - employee.calculate_total_deductions():.2f}. The tax to be paid is Nu.{tax:.2f}.")
