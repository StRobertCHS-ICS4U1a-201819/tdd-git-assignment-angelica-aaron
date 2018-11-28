def lowerQuartile(numlist: list) -> float:

    try:

        exceptionraiser = sum(numlist)

        numlist.sort()

        keyindex = len(numlist) // 4

        if len(numlist) % 4 == 2 or len(numlist) % 4 == 1:
            return numlist[keyindex]

        elif len(numlist) % 4 == 0:
            numone = numlist[keyindex]
            numtwo = numlist[keyindex - 1]
            return (numone + numtwo) / 2

    except IndexError:
        raise IndexError("The index is out of range.")

    except TypeError:
        raise TypeError("You did not input a list of integers.")

    except AttributeError:
        raise AttributeError("You did not input a list of integers.")