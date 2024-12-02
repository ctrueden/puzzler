import re

with open("day2.txt") as f:
    lines = f.readlines()

reports = [line.strip().split(" ") for line in lines]

def issafe(report):
    safesign = None
    for i in range(len(report) - 1):
        a = int(report[i])
        b = int(report[i + 1])
        dist = abs(b - a)
        if dist < 1 or dist > 3:
            return False
        sign = b - a > 0
        if safesign is None:
            safesign = sign
        else:
            if sign != safesign:
                return False
    return True

def can_be_safe(report):
    if issafe(report): return True
    for i in range(0, len(report)):
        variant = report[0:i] + report[i+1:]
        if issafe(variant): return True
    return False

#safe_reports = [report for report in reports if issafe(report)]
safe_reports = [report for report in reports if can_be_safe(report)]
print(len(safe_reports))
print(len(reports))
