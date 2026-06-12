import time
import primefac

from functools import cache

@cache
def isprime(p):
  return primefac.isprime(p)

def str2int(s: str) -> int:
  #return int(s, 16)  # base 16
  return int(s)  # base 10

def int2str(v: int) -> str:
  #return hex(v)[2:]  # base 16
  return str(v)  # base 10

def truncatable(p: int) -> bool:
  if not isprime(p): return False
  sp = int2str(p)
  n = len(sp)
  if n == 1: return False  # 2, 3, 5, 7
  for i in range(1, n):
    prefix = sp[0:i]
    if not isprime(str2int(prefix)): return False
    suffix = sp[n-i:n]
    if not isprime(str2int(suffix)): return False
  return True

start = time.time_ns()

num = 0
total = 0
for p in primefac.primegen():
  if truncatable(p):
    num += 1
    total += p
    print(p)
    if num >= 11: break

end = time.time_ns()

print(f"Total: {total}")
print(f"Time: {(end - start) // 1000000} ms")
