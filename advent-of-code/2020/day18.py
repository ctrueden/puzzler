import re

class Token:
  def __init__(self, v):
    self.v = v
  def __add__(self, other):
    return Token(self.v + other.v)
  def __sub__(self, other):
    return Token(self.v * other.v)
  def __str__(self):
    return str(self.v)
  def __int__(self):
      return self.v

def calc(e):
    e2 = exp.replace(" ", "").replace("*", "-")
    e3 = re.sub('(\\d+)', 'Token(\\1)', e2)
    return eval(e3)

with open("day18.txt") as f:
    exps = f.readlines()

sum = 0
for exp in exps:
    result = calc(exp)
    sum += int(calc(exp))

print(sum)
