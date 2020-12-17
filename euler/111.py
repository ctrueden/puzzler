import sympy
totaldigits = 10
total = 0
for digit in range(0, 10):
  total = 0
  for outlier in range(0, 10):
      if outlier == digit: continue
      for outlier_index in range(totaldigits):
          digits = []
          for _ in range(outlier_index):
              digits.append(digit)
          digits.append(outlier)
          for _ in range(outlier_index, totaldigits - 1):
              digits.append(digit)
          s = ''.join([str(d) for d in digits])
          if s.startswith('0'): continue
          num = int(s)
          if sympy.isprime(num):
              total += 1
              print(num)
  print(f'S({totaldigits}, {digit}) = {total}')

print(total)
