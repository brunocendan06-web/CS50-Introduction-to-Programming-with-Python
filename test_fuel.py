#import the program
import pytest
from fuel import convert, gauge

def test_convert_valid():
    assert convert("1/2") == 50
    assert convert("4/4") == 100
    assert convert("0/4") == 0

def test_convert_invalid_fraction():
    
    with pytest.raises(ValueError):
        convert("5/4")
 
    with pytest.raises(ValueError):
        convert("-1/4")
    
    with pytest.raises(ValueError):
        convert("1/-4")
  
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    
    with pytest.raises(ValueError):
        convert("a/4")
    with pytest.raises(ValueError):
        convert("1/b")

#gauge test
def test_gauge_empty_full():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_gauge_percentages():
    assert gauge(50) == "50%"
    assert gauge(25) == "25%"
    assert gauge(98) == "98%"