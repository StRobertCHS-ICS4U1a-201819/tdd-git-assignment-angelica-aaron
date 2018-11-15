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
        raise IndexError("The Index is Out of Range.")

    except TypeError:
        raise TypeRaiser("You Did Not Input a List of Integers.")

    except AttributeError:
        raise AttributeError("You Did Not Input a List of Integers.")
