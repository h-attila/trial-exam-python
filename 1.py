# Create a function that takes a list as a parameter,
# and returns a new list with all its element's values doubled.
# It should raise an error if the parameter is not a list.


def listValuesDubler(inputList):

    newList = []
    if type(inputList) == list:
        for item in inputList:
            newList.append(item*2)
    else:
        raise TypeError('only list type input accepted!')
    return newList


testList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(listValuesDubler(testList))

testFakeList = 'alma'
print(listValuesDubler(testFakeList))

