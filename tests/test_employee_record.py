# test_employee_record.py
"""Tests for the module test_employee_record.py"""

from employee_record import Employee


class TestEmployeeRecord:
    employee_basic = Employee("joe", "sales", 20, 20, 130.0, 130.0)
    employee_no_extra = Employee("joe", "sales", 20, 0, 130.0, 130.0)
    employee_zero = Employee("joe", "sales", 0, 0, 0, 0)
    employee_string = Employee("joe", "sales", 20, 20, 130.0, 130.0)

    def test_calculate_salary_basic(self):
        assert self.employee_basic.calculate_salary() == 5200

    def test_calculate_salary_no_extra(self):
        assert self.employee_no_extra.calculate_salary() == 2600

    def test_calculate_salary_zero(self):
        assert self.employee_zero.calculate_salary() == 0

    def test_str_contains_name_and_department(self):
        assert (
            str(self.employee_string)
            == "Employee: joe\nDepartment: sales\nWorking hours: 20\nExtra Working hours: 20\nFixed hour salary: 130.0\nExtra hour salary: 130.0"
        )
