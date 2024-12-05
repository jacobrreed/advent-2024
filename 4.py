with open("inputs/4.txt", "r") as f:
  data = f.read().strip().split("\n")

n = len(data)
m = len(data[0])

def has_xmas(i, j, d):
    dx, dy = d
    for k, x in enumerate("XMAS"):
        ii = i + k * dx
        jj = j + k * dy
        if not (0 <= ii < n and 0 <= jj < m):
            return False
        if data[ii][jj] != x:
            return False
    return True

def has_xmas_pt2(i, j):
    if not (1 <= i < n - 1 and 1 <= j < m - 1):
        return False
    if data[i][j] != "A":
        return False

    # Check both diagonals
    diag_1 = f"{data[i-1][j-1]}{data[i+1][j+1]}"
    diag_2 = f"{data[i-1][j+1]}{data[i+1][j-1]}"

    return diag_1 in ["MS", "SM"] and diag_2 in ["MS", "SM"]

def part1():
  n = len(data)
  m = len(data[0])

  # Generate all directions
  dd = []
  for dx in range(-1, 2):
      for dy in range(-1, 2):
          if dx != 0 or dy != 0:
              dd.append((dx, dy))
  # Count up every cell and every direction
  result = 0
  for i in range(n):
    for j in range(m):
        for d in dd:
            result += has_xmas(i, j, d)
  print(result)

def part2():
  dd = []
  for dx in range(-1, 2):
    for dy in range(-1, 2):
        if dx != 0 or dy != 0:
            dd.append((dx, dy))
  result = 0
  for i in range(n):
      for j in range(m):
          result += has_xmas_pt2(i, j)

  print(result)

part1()
part2()