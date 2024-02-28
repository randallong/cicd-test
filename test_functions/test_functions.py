import pytest
from ..functions.functions import function1, function2


def test_function1():
    x = function1()
    assert x == 1, "test failed"


def test_function2():
    x = function1()
    y = function2(x)
    assert y == 2, "test failed"
