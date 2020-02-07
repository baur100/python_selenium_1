from another import Another


def test_prime():
    # Arrange
    number_19 = Another(19)

    # Act
    result = number_19.f_prime()

    # Assert
    assert result == True


def test_prime_2():
    number_1 = Another(1)
    result = number_1.f_prime()
    assert result == False


def test_celsius():
    celsius_t_1 = Another(0)
    result = celsius_t_1.c_to_f()
    assert result == -17.77777777777778


def test_celsius_2():
    celsius_t_2 = Another(100)
    result = celsius_t_2.c_to_f()
    assert result == 37.77777777777778
