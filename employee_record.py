# employee_record.py
"""This module is used to calculate a simple employee record"""


class Employee:
    """This is the employee class."""

    def __init__(
        self,
        name: str,
        department: str,
        working_hours: int,
        extra_working_hours: int,
        fixed_hour_salary: float,
        extra_hour_salary: float,
    ):
        """The Employee class will be used do define the object.

        Args:
            name (str): full employee name
            department (str): employee working department
            working_hours (int): integer working hours (no float hours)
            extra_working_hours (int): integer working hours (no float hours)
            fixed_hour_salary (float): float with only 2 decimal cases
            extra_hour_salary (float): float with only 2 decimal cases
        """
        self.name = name
        self.department = department
        self.working_hours = working_hours
        self.extra_working_hours = extra_working_hours
        self.fixed_hour_salary = fixed_hour_salary
        self.extra_hour_salary = extra_hour_salary

    def calculate_salary(self) -> float:
        """This function calculates the full salary
        Returns:
        full_salary: float
        """
        fixed_salary = self.working_hours * self.fixed_hour_salary
        extra_salary = self.extra_working_hours * self.extra_hour_salary
        return fixed_salary + extra_salary

    def __str__(self) -> str:
        return f"Employee: {self.name}\nDepartment: {self.department}\nWorking hours: {self.working_hours}\nExtra Working hours: {self.extra_working_hours}\nFixed hour salary: {self.fixed_hour_salary}\nExtra hour salary: {self.extra_hour_salary}"


def main() -> None:
    """User I/O"""
    # Testing variables
    while True:
        try:
            name = str(input("Enter the employee name: "))
            if len(name) > 70:
                raise ValueError("Lenght name must be under 70 characters")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Try again.")
    while True:
        try:
            department = str(input("Enter the employee department: "))
            if len(department) > 20:
                raise ValueError("Department lenght must be under 20 characters")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Try again.")
    while True:
        try:
            working_hour = int(input("Enter the employee working hours: "))
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Try again.")
    while True:
        try:
            extra_working_hours = int(input("Enter the employee extraworking hours: "))
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Try again.")
    while True:
        try:
            fixed_hour_salary = float(input("Enter the employee fixed hour salary: "))
            fixed_hour_salary = float(round(fixed_hour_salary, 2))
            break
        except ValueError:
            print("Invalid input: please enter a number. Try again.")

    while True:
        try:
            extra_hour_salary = float(input("Enter the employee extra hour salary: "))
            extra_hour_salary = float(round(extra_hour_salary, 2))
            break
        except ValueError:
            print("Invalid input: please enter a number. Try again.")

    employee = Employee(
        name,
        department,
        working_hour,
        extra_working_hours,
        fixed_hour_salary,
        extra_hour_salary,
    )
    print(employee)
    print(f"{employee.name}'s salary is US${employee.calculate_salary():.2f}")


if __name__ == "__main__":
    main()
