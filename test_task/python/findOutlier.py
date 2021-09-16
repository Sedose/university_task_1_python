
def findOutlier(ints):
    if hasEvenTune(ints):
        return next(filter(isOdd, ints))
    else:
        return next(filter(isEven, ints))


def hasEvenTune(ints):
    return sum(isEven(x) for x in ints[0: 3]) > 1


def isEven(x):
  return x % 2 == 0


def isOdd(x):
  return not isEven(x)


#test
print(findOutlier([2, 4, 2, 6, 24, 14, 3]))
print(findOutlier([1, 55, 3, 15, 7, 4, 3]))
