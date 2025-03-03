import pytest
from employee import Employee

@pytest.fixture
def test_employee():
    test_employee = Employee("Jacob", "Kustra", 65000)
    return test_employee

def test_give_default_raise(test_employee):
    test_employee.give_raise()
    assert test_employee.salary == 70000

def test_give_custom_raise(test_employee):
    test_employee.give_raise(35000)
    assert test_employee.salary == 100000
