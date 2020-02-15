from some_class import SomeClass

def test_check_odd_or_even_number():
    #Arrange
    obj1=SomeClass(5, "cat", 11)
    #Act
    results=obj1.check_odd_or_even_number()
    #Assert
    assert results=="Odd"

def test_sum_number_anotherNumber():
    obj2=SomeClass(5, "dog", 4)
    results=obj2.sum_number_anotherNumber()
    assert results==9

def test_check_CapitalString():
    obj3=SomeClass(6, "School", 4)
    results=obj3.check_CapitalString()
    assert results




