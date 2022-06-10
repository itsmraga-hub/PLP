from itertools import permutations

numbers = [5, 6, 7, 8, 9]

numbers2 = [5, 6, 6, 7, 8]

def test(nums):
    """A function that takes a sequence of numbers and determines whether the numbers are different from each other."""
    if len(nums) == len(set(nums)):
        return "The numbers are different from each other"
    else:
        return "There are numbers which are not different"


# print(test(numbers))
# print(test(numbers2))


def createString():
    """A program to create all possible strings by using a, e, i, o u. Use the characters exactly once."""
    vowels = ['a', 'e', 'i', 'o', 'u']
    possibleStrings = permutations(vowels)

    for string in possibleStrings:
        print(''.join(string))

createString()

def removeThirdNumber(nums):
    """A program to remove and print every third number from a list of numbers till its empty"""
    position = 3 - 1
    i = 0
    length = len(nums)

    while length > 0:
        i = (position + i) % length
        print(nums.pop(i))
        length -= 1


removeThirdNumber(numbers)
