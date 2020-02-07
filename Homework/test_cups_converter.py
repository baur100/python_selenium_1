from cup import Cup

def test_cup_oz_convert():
    # Arrange
    cup = Cup(2)
    # Act
    result = cup.cup_oz_convert()
    # Assert
    assert result == 16

def test_cup_tablespoon_convert():
    # Arrange
    cup = Cup(3)
    # Act
    result = cup.cup_tablespoon_convert()
    # Assert
    assert result == 48

def test_cup_gallon_convert():
    # Arrange
    cup = Cup(5)
    # Act
    result = cup.cup_gallon_convert()
    # Assert
    assert result == 1.25