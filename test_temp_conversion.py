from temp_conversion import fahr_to_kelvin
from nose.tools import *

def test_run_1():
    assert fahr_to_kelvin (40) == 277.59444444444443

def test_run_2():
    assert fahr_to_kelvin('nn') == 0
    
def test_run_3():
    assert round(fahr_to_kelvin(-459.67),2) == 0.00 
#    assert fahr_to_kelvin(-459.67) == 0.00     
#def test_run_4():
#    assert fahr_to_kelvin() == 0.0  

@raises(TypeError)
def test_temp_string():
    assert fahr_to_kelvin("SomeTemperature")
    
@raises(TypeError)
def test_temp_null():
    assert fahr_to_kelvin()
    
