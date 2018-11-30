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

def upperQuartile(numlist: list) -> float:

   try:
       exceptionRaiser = sum(numlist)

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

def mean(numlist):

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

   try:
       totalrange = max(alist) - min(alist)
       return totalrange

   except:
       return "Invalid Input"
