arr1 = []
arr2 = []
with open("input.txt", "r") as file:
    for line in file:
        split = line.split()
        arr1.append(int(split[0]))
        arr2.append(int(split[1]))
    
arr1.sort()
arr2.sort()
answer = 0
# part 1
# for a1, a2 in zip(arr1, arr2):
#     answer += abs(a1-a2)

# part 2
for num in arr1:
    count = arr2.count(num)
    answer += num * count

print(answer)