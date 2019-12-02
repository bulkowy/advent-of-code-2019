def calc_fuel(mass):
  res = mass // 3 - 2
  if res <= 0:
    return 0
  return res + calc_fuel(res)

def extract_mass(string):
  return int(string.strip())

def result():
  res = 0
  with open('masses.txt', 'r') as f:
    for line in f:
      res += calc_fuel(extract_mass(line))

  return res

print(result())
