''' Tests '''
import pytest
from calculator import Calculator, Calculation

@pytest.fixture
def calc_with_fake_data(fake_data):
    """Fixture to create a Calculator instance using fake data."""
    calculator = Calculator()
    Calculator.clear_history()  # Clear previous history

    for record in fake_data:
        if record["operation"] == "add":
            calculator.add(record["operand1"], record["operand2"])
        elif record["operation"] == "subtract":
            calculator.subtract(record["operand1"], record["operand2"])
        elif record["operation"] == "multiply":
            calculator.multiply(record["operand1"], record["operand2"])
        elif record["operation"] == "divide":
            if record["operand2"] == 0:
                with pytest.raises(ZeroDivisionError):
                    calculator.divide(record["operand1"], record["operand2"])
            else:
                calculator.divide(record["operand1"], record["operand2"])

    return calculator

# Tests for Calculator operations
def test_add(calc_with_fake_data):
    """Test the add function using fake data."""
    for record in calc_with_fake_data.get_history():
        if record.operation == "add":
            assert record.result == record.operands[0] + record.operands[1]

def test_subtract(calc_with_fake_data):
    """Test the subtract function using fake data."""
    for record in calc_with_fake_data.get_history():
        if record.operation == "subtract":
            assert record.result == record.operands[0] - record.operands[1]

def test_multiply(calc_with_fake_data):
    """Test the multiply function using fake data."""
    for record in calc_with_fake_data.get_history():
        if record.operation == "multiply":
            assert record.result == record.operands[0] * record.operands[1]

def test_divide(calc_with_fake_data):
    """Test the divide function using fake data."""
    for record in calc_with_fake_data.get_history():
        if record.operation == "divide":
            if record.operands[1] == 0:
                continue  # Skip zero division check as it's handled in calc_with_fake_data
            assert record.result == record.operands[0] / record.operands[1]

def test_history(calc_with_fake_data):
    """Test that calculation history stores calculation instances correctly."""
    history = calc_with_fake_data.get_history()
    assert len(history) > 0  # Ensuring history is populated
    for record in history:
        assert isinstance(record, Calculation)

def test_clear_history(calc_with_fake_data):
    """Test that the clear_history method empties the calculation history."""
    calc_with_fake_data.clear_history()
    assert len(calc_with_fake_data.get_history()) == 0

def test_get_last_calculation(calc_with_fake_data):
    """Test that get_last_calculation retrieves the most recent calculation."""
    last_calc = calc_with_fake_data.get_last_calculation()
    assert last_calc is not None  # Ensuring last calculation is available
    assert isinstance(last_calc, Calculation)

def test_get_calculations_by_type(calc_with_fake_data):
    """Test that get_calculations_by_type filters history by operation type."""
    addition_calcs = calc_with_fake_data.get_calculations_by_type("add")
    assert len(addition_calcs) > 0  # Check if there are addition calculations

def test_get_last_calculation_empty_history():
    """Test that get_last_calculation raises IndexError when history is empty."""
    calculator = Calculator()
    calculator.clear_history()  # Ensuring history is cleared
    with pytest.raises(IndexError, match="No calculations in history."):
        calculator.get_last_calculation()

# New tests for Calculation methods
def test_calculation_str():
    """Test the __str__ method of the Calculation class."""
    calc = Calculation("add", [1, 2], 3)
    assert str(calc) == "Add: [1, 2] = 3"

def test_calculation_get_operands():
    """Test the get_operands method of the Calculation class."""
    calc = Calculation("subtract", [5, 3], 2)
    assert calc.get_operands() == [5, 3]

def test_calculation_get_result():
    """Test the get_result method of the Calculation class."""
    calc = Calculation("multiply", [2, 3], 6)
    assert calc.get_result() == 6

# Updated invalid input tests
@pytest.mark.parametrize("operation", ["add", "subtract", "multiply", "divide"])
def test_invalid_operand_types(calc_with_fake_data, operation):
    """Test that invalid operand types raise ValueError."""
    calculator = calc_with_fake_data  # Use the calculator with fake data
    with pytest.raises(ValueError, match="Operands must be numeric."):
        if operation == "add":
            calculator.add("string", 2)
        elif operation == "subtract":
            calculator.subtract("string", 2)
        elif operation == "multiply":
            calculator.multiply("string", 2)
        elif operation == "divide":
            calculator.divide("string", 2)

    with pytest.raises(ValueError, match="Operands must be numeric."):
        if operation == "add":
            calculator.add(2, None)
        elif operation == "subtract":
            calculator.subtract(2, None)
        elif operation == "multiply":
            calculator.multiply(2, None)
        elif operation == "divide":
            calculator.divide(2, None)
