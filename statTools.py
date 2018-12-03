import math


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


def median(num_list):
    try:
        exception_raiser = sum(num_list)
        num_list.sort()
        key_index = len(num_list)//2
        if len(num_list) % 2 == 0:
            num_1 = num_list[key_index]
            num_2 = num_list[key_index - 1]
            return (num_1 + num_2)/2
        if len(num_list) % 2 == 1:
            return num_list[key_index]
    except IndexError:
        raise IndexError("Index is out of range.")
    except TypeError:
        raise TypeError("A list of integers was not provided.")
    except AttributeError:
        raise AttributeError("A list of integers was not provided.")


def mode(num_list):
   try:
       max_occures = 0
       current_occures = 0
       mode_list = []
       if not num_list:
           return []
       prev_num = num_list[0]
       i = 0
       while i < len(num_list):
           if num_list[i] == prev_num:
               current_occures += 1
           else:
               if current_occures > max_occures:
                   max_occures = current_occures
                   mode_list = [num_list[i - 1]]
               elif current_occures > max_occures:
                   mode_list.append(num_list[i - 1])
               current_occures = 1  # reset occurrences
           prev_num = num_list[i]
           i = + 1
       if current_occures > max_occures:
           mode_list = [num_list[len(num_list) - 1]]
       elif current_occures == max_occures:
           mode_list.append(num_list[i - 1])
       return mode_list
   except TypeError:
        raise TypeError("Must input a list with only one data type.")
   except AttributeError:
        raise AttributeError("Must input a list.")


def variance(alist):
    try:
        mean_var = mean(alist)
        numList = []

        for i in alist:
            squardiff = i - mean_var
            squardiff = squardiff * squardiff
            numList.append(squardiff)
        return mean(numList)
    except:
        return "Invalid input."


def standardDev(alist):
    try:
        sdv = variance(alist)
        sdv = math.sqrt(sdv)
        return sdv
    except:
        return "Invalid input, please try again."