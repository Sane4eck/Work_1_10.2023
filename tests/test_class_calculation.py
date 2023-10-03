from Work_1 import *
import pytest


@pytest.mark.parametrize("a, b, expected_result", [(2, 5, 7),
                                                   (5, 9, 14),
                                                   (2, 2, 4)])
def test_summ_good(a, b, expected_result):
    oject_class = Calculation(var1=a, var2=b)
    var = oject_class.plus()
    assert var == expected_result
