import re
with open("inputs/3.txt", "r") as f:
  data = f.read().strip()

def part1():
  matches = re.findall(r"mul\((\d+),(\d+)\)", data)
  result = 0
  for match in matches:
    result += int(match[0]) * int(match[1])
  print(result)

def part2():
  matches = re.findall(r"(?:mul\((\d+),(\d+)\))|(do\(\)|don't\(\))", data)
  enabled = True
  result = 0
  for match in matches:
      if match[2] == "" and enabled:
          result += int(match[0]) * int(match[1])
      else:
          if match[2] == "do()":
              enabled = True
          else:
              enabled = False
  print(result)

part1()
part2()