from helpers.helperUtils import *
def solve_part_one():
    arr = readLineOfIntsToArr("day2.txt")
    answer = 0
    for report in arr:
        ans = analyze_report(report)
        print(ans, " ",report)
        answer += ans
    print(answer)

def analyze_report(arr):
    prev = arr[0]
    positive = False
    negative = False
    for i in range(1,len(arr)):
        if prev - arr[i] > 0:
            positive = True
        else:
            negative = True
        val = abs(prev - arr[i])
        if val == 0:
            return 0
        if val > 3:
            return 0
        prev = arr[i]
    if positive and negative:
        return 0
    return 1

def analyze_report_2(arr):
    first_pass = analyze_report(arr)
    if first_pass == 1:
        return 1
    errors = 0
    for i in range(len(arr)):
        combination = arr[:i] + arr[i + 1:]
        ans = analyze_report(combination)
        if ans == 0:
            errors += 1
        else:
            return 1
    if errors > 1:
        return 0
    else:
        return 1

def solve_part_two():
    arr = readLineOfIntsToArr("day2.txt")
    answer = 0
    for report in arr:
        ans = analyze_report_2(report)
        print(ans, " ",report)
        answer += ans
    print(answer)

solve_part_one()
solve_part_two()