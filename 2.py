# Read file into lines
with open("inputs/2.txt", "r") as f:
  lines = f.read().strip().split("\n")

def is_safe(numbers):
    inc = numbers[1] > numbers[0]
    if inc:
        for i in range(1, len(numbers)):
            diff = numbers[i] - numbers[i-1]
            if not 1 <= diff <= 3:
                return False
        return True
    else:
        for i in range(1, len(numbers)):
            diff = numbers[i] - numbers[i-1]
            if not -3 <= diff <= -1:
                return False
        return True

def is_really_safe(nums):
    if is_safe(nums):
        return True
    for i in range(len(nums)):
        if is_safe(nums[:i] + nums[i+1:]):
            return True
    return False

def part1():
  ans = 0
  for line in lines:
    nums = [int(i) for i in line.split()]
    ans += is_safe(nums)
  print(ans)

def part2():
  ans = 0
  for line in lines:
    nums = [int(i) for i in line.split()]
    ans += is_really_safe(nums)
  print(ans)


part1()
part2()