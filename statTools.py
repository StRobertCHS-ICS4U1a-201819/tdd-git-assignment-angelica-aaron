def lowerQuartile(numlist: list) -> float:

    try:

        exceptionRaiser = sum(numlist)

        numlist.sort()

        keyindex = len(numlist) // 4

        if len(numlist) % 4 == 2 or len(numlist) % 4 == 1:
            return numlist[keyindex]

        elif len(numlist) % 4 == 0:
            numOne = numlist[keyindex]
            numTwo = numlist[keyindex - 1]
            return (numOne + numTwo) / 2

    except IndexError:
        raise IndexError("The index is out of range.")

    except TypeError:
        raise TypeError("You did not input a list of integers.")

    except AttributeError:
        raise AttributeError("You did not input a list of integers.")


def upperQuartile(numlist: list) -> float:

    try:
        exceptionRaiser = sum(numlist)

        numlist.sort()

        keyindex = (len(numlist) - 1) - (len(numlist) // 4)

        if len(numlist) % 4 == 2 or len(numlist) % 4 == 1:
            return numlist[keyindex]

        elif len(numlist) % 4 == 3:
            numOne = numlist[keyindex]
            numTwo = numlist[keyindex + 1]
            return (numOne + numTwo) / 2

    except IndexError:
        raise IndexError("The index is out of range.")

    except TypeError:
        raise TypeError("You did not input a list of integers.")

    except AttributeError:
        raise AttributeError("You did not input a list of integers.")