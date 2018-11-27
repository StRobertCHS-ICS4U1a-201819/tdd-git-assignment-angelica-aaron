import pytest
from statTools import *

test_list_1 = [1, 2, 3, 4]
test_list_2 = [1, 2, 3, 6, 7]
test_list_3 = [1, 2, 5, 4, 6, 3, 7]
test_list_4 = [1, 2, 3, 4, 5]
test_list_5 = [1]
test_list_6 = [1, 4, 5]
test_list_7 = [2, 3, 4, 5]
test_empty_list = []
test_char_list = 'b'
test_str_list = ['a', 'b', 'c', 'd']

def test_median_1():
    assert (median(test_list_1) == 2.5) # corner case

def test_median_2():
    assert (median(test_list_3) == 4) # general case

def test_median_3():
    assert (median(test_list_5) == 1) # corner case

def test_median_not_list():
    with pytest.raises(TypeError) as errmsg:
        median(test_str_list)
    assert ('a list of intergers was not provided' == str(errmsg.value))

def test_median_string_list():
    with pytest.raises(TypeError) as errmsg:
        median(test_char_list)
    assert ('a list of intergers was not provided' == str(errmsg.value))

def test_median_empty_list():
    with pytest.raises(IndexError) as errmsg:
        median(test_empty_list)
    assert ('index is out of range' == str(errmsg.value))

