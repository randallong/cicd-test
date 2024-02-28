import pytest


def function1():
    x = 1
    return x


def function2(x):
    return x*2


def test_function1():
    x = function1()
    assert x == 1, "test failed"


def test_function2():
    x = function1()
    y = function2(x)
    assert y == 2, "test failed"
