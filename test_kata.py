
from kata import add 
import pytest

#1
def test_empty_string():
    assert add("") == 0

#2
def test_int():
    assert add("14") == 14

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
def test_support_multiple_numbers():
    assert add("1,2,3,4,5,6,7,8,9,10,11") == 1+2+3+4+5+6+7+8+9+10+11

#5
def test_newline():
    assert add("1\n2,3") == 6

#6
def test_ignore_numbers_bigger_than_1000():
    assert add("1001,2") == 2

