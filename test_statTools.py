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

# test median

def test_median_1():
    assert (median(test_list_1) == 2.5) # corner case

def test_median_2():
    assert (median(test_list_3) == 4) # general case

def test_median_3():
    assert (median(test_list_5) == 1) # corner case

def test_median_not_list():
    with pytest.raises(TypeError) as errmsg:
        median(test_str_list)
    assert ("A list of integers was not provided." == str(errmsg.value))    # unusual case

def test_median_string_list():
    with pytest.raises(TypeError) as errmsg:
        median(test_char_list)
    assert ("A list of integers was not provided." == str(errmsg.value))    # unusual case

def test_median_empty_list():
    with pytest.raises(IndexError) as errmsg:
        median(test_empty_list)
    assert ("Index is out of range." == str(errmsg.value))  # unusual case

# test mode with own lists

def test_mode_1():
    assert (mode([1, 1, 2, 3]) == [1])   # general case

def test_mode_1():

def test_mode_2():
    assert (mode([1, 2, 2, 3, 3, 3, 4]) == [3]) # general case

def test_mode_3():
    assert (mode([3]) == [1])   # general case

def test_mode_4():
    assert (mode([]) == [])   # corner case

def test_mode_5():
    assert (mode([2, 2, 3, 3, 5]) == [1])   # corner case

def test_mode_string_list():
    assert (mode(['a', 'b', 'b', 'c']) == ['b'])

def test_mode_not_list():
    with pytest.raises(AttributeError) as errmsg:
        mode(1)
    assert ("Must input a list." == str(errmsg.value))  # unusual case

def test_mode_mult_data_type():
    with pytest.raises(TypeError) as errmsg:
        mode([2, 'b'])
    assert ("Must input a list with only one data type." == str(errmsg.value))  # unusual case

# test variance

def test_variance_1():
    assert (variance(test_list_1) == 2)

def test_variance_2():
    assert (variance(test_) == )

def test_variance_3():
    assert (variance(test_) == )

def test_variance_4():
    assert (variance(test_) == )

def test_variance_5():
    assert (variance(test_) == )

def test_variance_6():
    assert (variance(test_) == )

def test_variance_7():
    assert (variance(test_) == )
