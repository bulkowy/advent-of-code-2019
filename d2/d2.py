import copy
class Intcode:
  def __init__(self):
    self.pos = 0
    self.extract_states('vals.txt')
    self.codes = [1, 2, 99]

  def reset_memory(self):
    self.pos = 0
    self.states = copy.deepcopy(self.main_memory)

  def extract_states(self, filename):
    with open(filename, 'r') as f:
      self.main_memory = [int(x) for x in f.readline().strip().split(',')]

  def extract_op(self):
    if self.states[self.pos] == 99:
      return [99]
    elif self.states[self.pos] in [1,2]:
      return self.states[self.pos:self.pos+4]
    else:
      raise Exception("unknown")

  def process(self):
    cur_op = self.extract_op()
    if cur_op[0] == 99:
      raise Exception("ended")

    if cur_op[0] == 1:
      self.states[cur_op[3]] = self.states[cur_op[1]] + self.states[cur_op[2]]

    else:
      self.states[cur_op[3]] = self.states[cur_op[1]] * self.states[cur_op[2]]

  def make_step(self):
    self.pos += 4

  def loop(self):
    while True:
      try:
        self.process()
        self.make_step()
      except Exception as e:
        #print(e)
        break


a = Intcode()

for noun in range(0,99):
  for verb in range(0,99):
    a.reset_memory()
    a.states[1] = noun
    a.states[2] = verb
    a.loop()
    if a.states[0] == 19690720:
      print(a.states[0], noun, verb)
