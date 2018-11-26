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


def upperQuartile(numlist: list) -> float:

    try:
        exceptionraiser = sum(numlist)

        numlist.sort()

        keyindex = (len(numlist) - 1) - (len(numlist) // 4)

        if len(numlist) % 4 == 2 or len(numlist) % 4 == 1:
            return numlist[keyindex]

        elif len(numlist) % 4 == 3:
            numone = numlist[keyindex]
            numtwo = numlist[keyindex + 1]
            return (numone + numtwo) / 2

    except IndexError:
        raise IndexError("The index is out of range.")

    except TypeError:
        raise TypeError("You did not input a list of integers.")

    except AttributeError:
        raise AttributeError("You did not input a list of integers.")

def mean(numlist)

    try:
        listclone = numlist

        numbersum = 0

        for item in listclone:

            numbersum = numbersum + item

        finalnum = numbersum / len(numlist)

        return finalnum

    except:
        return "Invalid Input"


def numrange(alist):

    try:
        totalrange = max(alist) - min(alist)
        return totalrange

    except:
        return "Invalid Input"