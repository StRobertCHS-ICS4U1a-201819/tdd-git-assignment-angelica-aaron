#----------------------------------------------------------------------------------------------
# Name: statTools.py
# Purpose: Mathematical functions
#
# Author: Ramos-Cortes A.
#
# Date: 29 December 2018
#----------------------------------------------------------------------------------------------
def lowerQuartile(numlist: list) -> float:
    """Find the lower quartile for a list

    :param numlist:
    :return: lower quartile
    """

    try:

        exceptionRaiser = sum(numlist)

        numlist.sort()

        keyIndex = len(numlist) // 4

        if len(numlist) % 4 == 2 or len(numlist) % 4 == 1:
            return numlist[keyIndex]

        elif len(numlist) % 4 == 0:
            numOne = numlist[keyIndex]
            numTwo = numlist[keyIndex - 1]
            return (numOne + numTwo) / 2

    except IndexError:
        raise IndexError("The Index is Out of Range.")

    except TypeError:
        raise TypeError("You Did Not Input a List of Integers.")

    except AttributeError:
        raise AttributeError("You Did Not Input a List of Integers.")

def upperQuartile(numlist: list) -> float:
    """Find the upper quartile of a list

    :param numlist:
    :return: upper quartile
    """

    try:
        exceptionRaiser = sum(numlist)

        numlist.sort()

        keyIndex = (len(numlist) -1) - (len(numlist) // 4)

        if len(numlist) % 4 == 2 or len(numlist) % 4 == 1:
            return numlist[keyIndex]

        elif len(numlist) % 4 == 0:
            numOne = numlist[keyIndex]
            numTwo = numlist[keyIndex + 1]
            return (numOne + numTwo) / 2

        elif len(numlist) % 4 == 3:
            numOne = numlist[keyIndex]
            numTwo = numlist[keyIndex - 1]
            return (numOne + numTwo) / 2

    except IndexError:
        raise IndexError("The Index is Out of Range.")

    except TypeError:
        raise TypeError("You Did Not Input a List of Integers.")

    except AttributeError:
        raise AttributeError("You Did Not Input a List of Integers.")

def mean(numlist):
    """find the mean of a list

    :param numlist:
    :return: mean
    """

    try:
       listClone = numlist

       numberSum = 0

       for item in listClone:

           numberSum = numberSum + item

       finalNum = numberSum / len(numlist)

       return finalNum

    except:
       return "Invalid Input"


def numrange(alist):
    """finds the range of a list

    :param alist:
    :return: range
    """

    try:
        totalrange = max(alist) - min(alist)
        return totalrange

    except:
        return "Invalid Input"