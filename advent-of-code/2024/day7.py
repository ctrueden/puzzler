with open("day7.txt") as f:
    lines = [line.strip() for line in f.readlines()]


def calculate(operands, target):
    assert len(operands) > 0
    if len(operands) == 1:
        return int(operands[0]) == target
    return (
        calculate([str(int(operands[0]) + int(operands[1]))] + operands[2:], target) or
        calculate([str(int(operands[0]) * int(operands[1]))] + operands[2:], target) or
        calculate([operands[0] + operands[1]] + operands[2:], target)
    )


total = 0
for line in lines:
    result, operands = line.split(":")
    result = int(result)
    operands = [operand for operand in operands.strip().split(" ")]
    if calculate(operands, result):
        print(f"{result} {operands}")
        total += result
print(total)
