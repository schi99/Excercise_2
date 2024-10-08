### test_square

def square(x):  
    '''
    Input: x, a positive number
    Returns the square of a number
    '''
       
    x: float
    solution = x*x
    return(solution)

square(4.41)
   
import pytest

EPSILON = 0.0001

def test_square1():
    assert square(-2.8) == pytest.approx(7.839999999999999, EPSILON)

def test_square2():
 assert square(4.41) == pytest.approx(19.4481, EPSILON)

def test_square3():
   assert square(0.29) == pytest.approx(0.0841, EPSILON)

def test_square4():
   assert square(1.75) == pytest.approx(3.0625, EPSILON)

def test_square5():
   assert square(-4.96) == pytest.approx(24.6016, EPSILON)  