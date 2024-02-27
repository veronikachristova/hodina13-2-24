#pip install pytest
#iny sposob robenia testov nie cez triedu

import pytest
from lekcia16 import Kalkulacka

def test_add_integers():
    calc = Kalkulacka()
    assert calc.sucet(1,2) == 1

def test_add_negative():
    calc = Kalkulacka()
    assert calc.sucet(-1,-1) == -2

def test_add_floats():
    calc = Kalkulacka()
    assert calc.sucet(1.1,2.2) == pytest.approx(3.3)

