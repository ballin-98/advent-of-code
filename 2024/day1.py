from helpers import helperUtils

# read in the inputs and sort the arrays
arr1, arr2 = helperUtils.readTwoInts("day1.txt")
arr1.sort()
arr2.sort()

# return the difference between the two values
def solve_part_one(arr1, arr2):
    answer = 0
    for a1, a2 in zip(arr1, arr2):
        answer += abs(a1-a2)
    return answer

# return the number in arr1 * the number of times it occurs in arr2
def solve_part_two(arr1, arr2):
    answer = 0
    for num in arr1:
        count = arr2.count(num)
        answer += num * count
    return answer

partOne = solve_part_one(arr1, arr2)
partTwo = solve_part_two(arr1, arr2)
print(partOne)
print(partTwo)

