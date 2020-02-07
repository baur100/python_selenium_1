from homework.homework_1 import Countries

def ch():
    # ARRANGE
    china = Countries("China", 1439323776, 9388211, 153)
    # ACT
    result = china.county_pop()
    # ASSERT
    assert result == "overpopulated"

def usa():
    us = Countries("United State of America", 331002651, 9147420, 36)
    result = us.county_pop()
    assert us.county_pop() == ch()

def ua():
    ua = Countries("Ukraine", 43733762, 579320, 75)
    result = ua.country_dens()
    assert result == "Uzbekistan"
