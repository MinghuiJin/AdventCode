from collections import defaultdict

def parse_file(file_name):
    f = open(file_name, "r")
    lines = f.readlines()

    left_list, right_list = [], []
    for line in lines:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)
    return left_list, right_list

def solve_part1():
    left_list, right_list = parse_file("input1.txt")
    left_list.sort()
    right_list.sort()

    return sum(abs(l - r) for l, r in zip(left_list, right_list))

def solve_part2():
    left_list, right_list = parse_file("input1.txt")
    right_count = defaultdict(int)
    for num in right_list:
        right_count[num] = right_count.get(num, 0) + 1

    ans = 0
    for n in left_list:
        ans += n * right_count.get(n, 0)
    return ans

print(solve_part1())
print(solve_part2())
