from kata import add 

def test_empty_string():
    assert add("") == 0


def test_int():
    for i in range(0,100):
        assert add("i") == i

def test_support_two_numbers():
    assert add("1,2") == 3