import pytest
from car import Car

def test_gas_type():
        # Arrange
    volvo_s90 = Car("Volvo", "S90",2)
        # Act
    result = volvo_s90.convert_gas()
        # Assert
    assert result == "Regular", "Gas type is wrong"
