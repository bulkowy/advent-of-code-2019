def read_moves():
  with open('inputs.txt', 'r') as f:
    moves1 = [[m[0], int(m[1:])] for m in f.readline().strip().split(',')]
    moves2 = [[m[0], int(m[1:])] for m in f.readline().strip().split(',')]

  return moves1, moves2

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __repr__(self):
    return "P(" + str(self.x) + ", " + str(self.y) + ")"

def create_lines(moves):
  lines = [Point(0,0)]
  for move in moves:
    if move[0] == 'R':
      lines.append(Point(lines[-1].x, lines[-1].y + move[1]))
    elif move[0] == 'L':
      lines.append(Point(lines[-1].x, lines[-1].y - move[1]))
    elif move[0] == 'U':
      lines.append(Point(lines[-1].x + move[1], lines[-1].y))
    else:
      lines.append(Point(lines[-1].x - move[1], lines[-1].y))
  return lines

def ccw(A, B, C):
  return (C.y - A.y) * (B.x - A.x) > (B.y - A.y) * (C.x - A.x)

def intersect(A, B, C, D):
  return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)

def find_intersections(l1, l2):
  intersections = []
  paths = []
  units_l1 = 0
  for i in range(1, len(l1)):
    units_l2 = 0
    line1 = (l1[i-1], l1[i])
    l1_hor = True if line1[0].y == line1[1].y else False
    for j in range(1, len(l2)):
      line2 = (l2[j-1], l2[j])
      l2_hor = True if line2[0].y == line2[1].y else False
      if intersect(line1[0], line1[1], line2[0], line2[1]):
        if not l1_hor:
          intersections.append(Point(l1[i].x, l2[j].y))
        else:
          intersections.append(Point(l2[j].x, l1[i].y))
        paths.append(units_l1 + units_l2 + abs(line1[0].x - line2[0].x) + abs(line1[0].y - line2[0].y))
      units_l2 += abs(line2[0].x - line2[1].x) if l2_hor else abs(line2[0].y - line2[1].y)
    units_l1 += abs(line1[0].x - line1[1].x) if l1_hor else abs(line1[0].y - line1[1].y)
  print("min: " + str(min(paths)))
  return intersections


def find_min_manhattan(l):
  min = 9999999
  for e in l:
    tmp = abs(e.x) + abs(e.y)
    min = tmp if tmp < min else min
  return min

m1,m2 = read_moves()
lines1 = create_lines(m1)
lines2 = create_lines(m2)
print(find_min_manhattan(find_intersections(lines1, lines2)))
