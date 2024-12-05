# Read file 1.txt and for each line store the 1st number in list1 and the 2nd number in list2
# Then sort each list
# then compare the same index of each list to get the difference between numbers and add the difference to the total
# print the total out after reading all lines
# For each number in list1, check how many times it occurs in list2 and multiply the number from list1 by how many times it occurs, then add it to the totalSimilarityScore

list1 = []
list2 = []
total = 0
totalSimilarityScore = 0

with open("inputs/1.txt", "r") as f:
    for line in f:
        numbers = line.split()
        list1.append(int(numbers[0]))
        list2.append(int(numbers[1]))

list1.sort()
list2.sort()

for i in range(len(list1)):
    total += abs(list1[i] - list2[i])

for num in list1:
    count = list2.count(num)
    totalSimilarityScore += num * count

print("Total:", total)
print("Total Similarity Score:", totalSimilarityScore)
