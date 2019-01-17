#----------------------------------------------------------------------------------------------
# Name: statTools.py
# Purpose: tests mathematical functions
#
# Author: Ramos-Cortes A.
#
# Date: 30 December 2018
#----------------------------------------------------------------------------------------------

import pytest
from statTools import *

testList1 = [1, 2, 3, 4]
testList2 = [1, 2, 3, 4, 5, 6]
testList3 = [1, 2, 3, 4, 5, 6, 7]
testList4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
testList5 = [1, 2, 3]
testList6 = [1, 2]
testList7 = [1]
testEmptyList = []
testNotList = "a"
testStringList = ["a", "b", "c", "d", "e", "f", "g"]

def testLowerQ1():
    assert(lowerQuartile(testList1) == 1.5)  # corner case -- LQ is the average of 2 numbers


def testLowerQ2():
    assert(lowerQuartile(testList2) == 2)  # general case -- returns item from index in list


def testLowerQ3():
    assert (lowerQuartile(testList3) == 2.5)  # corner case -- LQ is the average of 2 numbers


def testLowerQ4():
    assert (lowerQuartile(testList4) == 3)  # general case -- returns item from index in list


def testLowerQ5():
    assert (lowerQuartile(testList5) == 1.5)  # corner case -- list smaller than 4 items


def testLowerQ6():
    assert (lowerQuartile(testList6) == 1)  # corner case -- list smaller than 4 items


def testLowerQ7():
    assert (lowerQuartile(testList7) == 1)  # corner case -- list smaller than 4 items


def testLowerQEmptyList():  # unusual case --  empty list
    with pytest.raises(IndexError) as errmsg:
        lowerQuartile(testEmptyList)
    assert ("index is out of range." == str(errmsg.value))


def testLowerQNotList():  # unusual case -- not a list
    with pytest.raises(TypeError) as errmsg:
        lowerQuartile(testNotList)
    assert ("A list of integers was not provided." == str(errmsg.value))


def testLowerQStringList():  # unusual case -- list of strings
    with pytest.raises(TypeError) as errmsg:
        lowerQuartile(testStringList)
    assert ("A list of integers was not provided." == str(errmsg.value))

# upper quartile tests


def testUpperQ1():
    assert (upperQuartile(testList1) == 3.5)  # corner case -- LQ is the average of 2 numbers


def testUpperQ2():
    assert (upperQuartile(testList2) == 5)  # general case -- returns item from index in list


def testUpperQ3():
    assert (upperQuartile(testList3) == 5.5)  # corner case -- LQ is the average of 2 numbers


def testUpperQ4():
    assert (upperQuartile(testList4) == 7)  # general case -- returns item from index in list


def testUpperQ5():
    assert (upperQuartile(testList5) == 2.5)  # corner case -- LQ is the average of 2 numbers


def testUpperQ6():
    assert (upperQuartile(testList6) == 2)  # corner case -- list smaller than 4 items


def testUpperQ7():
    assert (upperQuartile(testList7) == 1)  # corner case -- list smaller than 4 items


def testUpperQEmptyList():  # unusual case -- empty list
    with pytest.raises(IndexError) as errmsg:
        upperQuartile(testEmptyList)
    assert ("Index is out of range." == str(errmsg.value))


def testUpperQNotList():  # unusual case -- not a list
    with pytest.raises(TypeError) as errmsg:
        upperQuartile(testNotList)
    assert ("A list of integers was not provided." == str(errmsg.value))


def testUpperQStringList():  # unusual case -- list of strings
    with pytest.raises(TypeError) as errmsg:
        upperQuartile(testStringList)
    assert ("A list of integers was not provided." == str(errmsg.value))

def testMean1():
    assert(mean(testList1) == 2.5)


def testMean2():
    assert (mean(testList2) == 3.5)


def testMean3():
    assert (mean(testList3) == 4)


def testMean4():
    assert (mean(testList4) == 5)


def testMean5():
    assert (mean(testList5) == 2)

def testMean6():
    assert (mean(testList6) == 1.5)


def testMean7():
    assert (mean(testList7) == 1)


def testMeanEmptyList():
    with pytest.raises(IndexError) as errmsg:
        (mean(testEmptyList))
    assert ("Index is out of range." == str(errmsg.value))


def testMeanNotList():
    with pytest.raises(TypeError) as errmsg:
        (mean(testNotList))
    assert ("A list of integers was not provided." == str(errmsg.value))


def testMeanStringList():
    with pytest.raises(TypeError) as errmsg:
        (mean(testStringList))
    assert ("A list of integers was not provided." == str(errmsg.value))

# mean tests


def testRange1():
    assert (numrange(testList1) == 3)


def testRange2():
    assert (numrange(testList2) == 5)


def testRange3():
    assert (numrange(testList3) == 6)


def testRange4():
    assert (numrange(testList4) == 8)


def testRange5():
    assert (numrange(testList5) == 2)


def testRange6():
    assert (numrange(testList6) == 1)


def testRange7():
    assert (numrange(testList7) == 0)


def testRangeEmptyList():
    with pytest.raises(IndexError) as errmsg:
        (numrange(testEmptyList))
    assert ("Index is out of range." == str(errmsg.value))


def testRangeNotList():
    with pytest.raises(TypeError) as errmsg:
        (numrange(testNotList))
    assert ("A list of integers was not provided." == str(errmsg.value))


def testRangeStringList():
    with pytest.raises(TypeError) as errmsg:
        (numrange(testStringList))
    assert ("A list of integers was not provided." == str(errmsg.value))

# range tests