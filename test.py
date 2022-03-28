from kata import add 

#1
def test_empty_string():
    assert add("") == 0

#2
def test_int():
    for i in range(0,100):
        assert add("i") == i

#3
def test_support_two_numbers_1():
    assert add("1,2") == 3

def test_support_two_numbers_2():
    assert add("4,6") == 10

def test_support_two_numbers_3():
    for i in range(0,1000):
        for j in range(0,1000):
            assert add(f"{i},{j}") == i+j

#4
