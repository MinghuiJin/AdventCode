def parse_file(file_name):
    res = []
    file = open(file_name, "r")
    lines = file.readlines()
    for line in lines:
        res.append(list(map(int, line.split())))
    return res


def is_safe(report):
    if report[0] == report[1] or abs(report[1] - report[0]) > 3:
            return False

    ascending = report[1] - report[0] > 0

    for i in range(2, len(report)):
        if ascending and report[i] < report[i - 1]:
            return False
        
        if not ascending and report[i] > report[i - 1]:
            return False
        
        if not 1 <= abs(report[i] - report[i - 1]) <= 3:
            return False   
    return True


def solve_part1():
    ans = 0
    reports = parse_file("input2.txt")

    for report in reports:
        if is_safe(report):
            ans += 1
    return ans


'''
7 6 4 2 1: Safe without removing any level.
1 2 7 8 9: Unsafe regardless of which level is removed.
9 7 6 2 1: Unsafe regardless of which level is removed.
1 3 2 4 5: Safe by removing the second level, 3.
8 6 4 4 1: Safe by removing the third level, 4.
1 3 6 7 9: Safe without removing any level.
9 13 12 11: Safe by removing the first level, 9.
9 13 8 7: Safe by removing the secondg level, 1.


conditions:
safe without removing any level
unsafe regardless of which level is removed, when in asending/descending order
when two levels found equal, then remove one of it, then continue compare
when a level found as unsafe when the index is the last one, then just remove the last element, it is safe
when a level found as unsafe when the index is inside the list, then remove the level, then compare, the order is the level before it and the level afer it
'''
def solve_part2():
    reports = parse_file("input2.txt")
    ans = 0

    for report in reports:
        if is_safe(report):
            ans += 1
        else:
            # print(report)
            for i in range(len(report)):
                if is_safe(report[:i] + report[i + 1:]):
                    ans += 1
                    break
    return ans

if __name__ == "__main__":
    print(solve_part1())
    print(solve_part2())
