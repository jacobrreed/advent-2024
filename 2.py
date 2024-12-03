safe_count = 0
with open("2.txt", "r") as f:
    # for each line in the file, check that the numbers are either in ascending or descending order
    # if they are, check that the absolute difference between each number is > 1 and <= 3
    # If all conditions are met, increment the safe_count
    for line in f:
        numbers = line.split()
        numbers = list(map(int, numbers))
        ascending = True
        descending = True
        for i in range(1, len(numbers)):
            if numbers[i] < numbers[i-1]:
                ascending = False
            if numbers[i] > numbers[i-1]:
                descending = False
            if not ascending and not descending:
                break
            if abs(numbers[i] - numbers[i-1]) > 3:
                ascending = False
                descending = False
                break
        if ascending or descending:
            safe_count += 1
print(safe_count)