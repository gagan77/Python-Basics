import addition
import pytest

def test_add(): 
    
    assert addition.add(2,3) == 5
    
    
def test_sub(): # 
    assert addition.sub(2,3) == -1
    
# need to install pip package to use pytest
# python -m pytest test_addition.py:: test_add is used to run the test cases