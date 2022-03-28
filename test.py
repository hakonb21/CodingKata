from kata import add 

def test_empty_string():
    assert add("") == 0
    

def test_int():
    for i in range(0,100):
        assert kata("i") == i
