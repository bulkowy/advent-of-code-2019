input = (240298, 784956 + 1) # for range

def calculate(input):
  met = 0
  for x in range(input[0], input[1]):
    is_password = True
    digits = str(x)
    is_digit = None
    for offset in range(0, 5):
      if int(digits[offset:]) > (int(digits[offset+1:] + digits[-1])):
        is_password = False
        break
    if is_password:
      d = {}
      for c in digits:
        d[c] = 1 if c not in d else d[c] + 1
      #part1
      #for e in d.values():
      #  if e >= 2:
      #    met += 1
      #    break
      #part2
      met += 1 if 2 in d.values() else 0
  return met

print(calculate(input))
