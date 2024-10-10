#test_eval_quadratic

def eval_quadratic(a, b, c, x):

    """
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic

    """

    solution = a*(x*x) + b*x + c
    
    return(solution)

import pytest

EPSILON = 0.0001

def test_quadratic_1():
    assert eval_quadratic(-7.47, -2.32, 3.81, 3.86) == pytest.approx(-116.4452, EPSILON)

def test_quadratic_2():
    assert eval_quadratic(3.72, 2.76, 6.93, -2.69) == pytest.approx(26.4239, EPSILON)

def test_quadratic_3():
    assert eval_quadratic(-8.83, -4.93, -9.94, -3.86) == pytest.approx(-122.4737, EPSILON)

def test_quadratic_4():
    assert eval_quadratic(6.01, -2.48, -0.38, -0.23) == pytest.approx(0.5083, EPSILON)

def test_quadratic_5():
    assert eval_quadratic(-2.25, -9.7, 2.47, -0.36) == pytest.approx(5.6704, EPSILON)