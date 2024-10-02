''' Tests '''
import pytest
from calculator import Calculator, Calculation

@pytest.fixture
def calc_fixture():
    '''Fixture to create a new Calculator instance and clear history before each test.'''
    Calculator.clear_history()
    return Calculator()

# Tests for Calculator operations
@pytest.mark.parametrize("operand1, operand2, expected", [
    (1, 2, 3),
    (5, 3, 8),
    (-1, -1, -2)
])
def test_add(request, operand1, operand2, expected):
    '''Test the add function with different inputs and expected results.'''
    calculator = request.getfixturevalue('calc_fixture')
    assert calculator.add(operand1, operand2) == expected

@pytest.mark.parametrize("operand1, operand2, expected", [
    (5, 3, 2),
    (10, 5, 5),
    (0, 0, 0)
])
def test_subtract(request, operand1, operand2, expected):
    '''Test the subtract function with different inputs and expected results.'''
    calculator = request.getfixturevalue('calc_fixture')
    assert calculator.subtract(operand1, operand2) == expected

@pytest.mark.parametrize("operand1, operand2, expected", [
    (2, 3, 6),
    (-1, 5, -5),
    (0, 5, 0)
])
def test_multiply(request, operand1, operand2, expected):
    '''Test the multiply function with different inputs and expected results.'''
    calculator = request.getfixturevalue('calc_fixture')
    assert calculator.multiply(operand1, operand2) == expected

@pytest.mark.parametrize("operand1, operand2, expected", [
    (6, 3, 2),
    (-10, 2, -5),
    (5, 2, 2.5)
])
def test_divide(request, operand1, operand2, expected):
    '''Test the divide function with different inputs and expected results.'''
    calculator = request.getfixturevalue('calc_fixture')
    assert calculator.divide(operand1, operand2) == expected

def test_divide_by_zero(request):
    '''Test that dividing by zero raises a ZeroDivisionError.'''
    calculator = request.getfixturevalue('calc_fixture')
    with pytest.raises(ZeroDivisionError):
        calculator.divide(6, 0)

def test_history(request):
    '''Test that calculation history stores calculation instances correctly.'''
    calculator = request.getfixturevalue('calc_fixture')
    calculator.add(1, 1)
    calculator.subtract(2, 1)
    history = calculator.get_history()
    assert len(history) == 2
    assert isinstance(history[0], Calculation)
    assert isinstance(history[1], Calculation)

def test_clear_history(request):
    '''Test that the clear_history method empties the calculation history.'''
    calculator = request.getfixturevalue('calc_fixture')
    calculator.add(1, 1)
    calculator.clear_history()
    assert len(calculator.get_history()) == 0

def test_get_last_calculation(request):
    '''Test that get_last_calculation retrieves the most recent calculation.'''
    calculator = request.getfixturevalue('calc_fixture')
    calculator.add(1, 1)
    calculator.subtract(2, 1)
    last_calc = calculator.get_last_calculation()
    assert last_calc.operation == "subtract"
    assert last_calc.result == 1
    assert last_calc.operands == [2, 1]  # Check operands as well

def test_get_calculations_by_type(request):
    '''Test that get_calculations_by_type filters history by operation type.'''
    calculator = request.getfixturevalue('calc_fixture')
    calculator.add(1, 1)
    calculator.subtract(2, 1)
    addition_calcs = calculator.get_calculations_by_type("add")
    assert len(addition_calcs) == 1
    assert addition_calcs[0].operation == "add"

def test_get_last_calculation_empty_history(request):
    '''Test that get_last_calculation raises IndexError when history is empty.'''
    calculator = request.getfixturevalue('calc_fixture')
    with pytest.raises(IndexError, match="No calculations in history."):
        calculator.get_last_calculation()

# New tests for Calculation methods
def test_calculation_str():
    '''Test the __str__ method of the Calculation class.'''
    calc = Calculation("add", [1, 2], 3)
    assert str(calc) == "Add: [1, 2] = 3"

def test_calculation_get_operands():
    '''Test the get_operands method of the Calculation class.'''
    calc = Calculation("subtract", [5, 3], 2)
    assert calc.get_operands() == [5, 3]

def test_calculation_get_result():
    '''Test the get_result method of the Calculation class.'''
    calc = Calculation("multiply", [2, 3], 6)
    assert calc.get_result() == 6

def test_invalid_addition_inputs(request):
    '''Test that add raises ValueError for invalid operand types.'''
    calculator = request.getfixturevalue('calc_fixture')
    with pytest.raises(ValueError, match="Operands must be numeric."):
        calculator.add("string", 2)  # Invalid type
    with pytest.raises(ValueError, match="Operands must be numeric."):
        calculator.add(2, None)  # Invalid type

def test_invalid_subtraction_inputs(request):
    '''Test that subtract raises ValueError for invalid operand types.'''
    calculator = request.getfixturevalue('calc_fixture')
    with pytest.raises(ValueError, match="Operands must be numeric."):
        calculator.subtract("string", 2)  # Invalid type
    with pytest.raises(ValueError, match="Operands must be numeric."):
        calculator.subtract(2, None)  # Invalid type

def test_invalid_multiplication_inputs(request):
    '''Test that multiply raises ValueError for invalid operand types.'''
    calculator = request.getfixturevalue('calc_fixture')
    with pytest.raises(ValueError, match="Operands must be numeric."):
        calculator.multiply("string", 2)  # Invalid type
    with pytest.raises(ValueError, match="Operands must be numeric."):
        calculator.multiply(2, None)  # Invalid type

def test_invalid_division_inputs(request):
    '''Test that divide raises ValueError for invalid operand types.'''
    calculator = request.getfixturevalue('calc_fixture')
    with pytest.raises(ValueError, match="Operands must be numeric."):
        calculator.divide("string", 2)  # Invalid type
    with pytest.raises(ValueError, match="Operands must be numeric."):
        calculator.divide(2, None)  # Invalid type
