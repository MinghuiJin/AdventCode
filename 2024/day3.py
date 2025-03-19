def find_mul(idx, file):
    closed, found_comma = False, False
    i = idx
    while i < len(file):
        char = file[i]
        if not char.isdigit() and char not in ',)':
            break
        
        if char == "," and not found_comma:
            found_comma = True
        elif char == ',' and found_comma:
            break

        if char == ')':
            closed = True
            if found_comma:
                nums1, nums2 = list(map(int, file[idx:i].split(',')))
                break
            else:
                break
        
        i += 1

    if not closed:
        return None

    return nums1 * nums2 if nums1 is not None and nums2 is not None else None

def solve_part1(file):
    ans = 0
    for i in range(len(file)):
        if file[i : i + 4] == "mul(":
            temp = find_mul(i + 4, file)
            if temp is not None:
                ans += temp
    return ans

def solve_part2(file):
    ans = 0
    enabled = True
    i = 0
    while i < len(file):
        if file[i:i+len("don't()")] == "don't()":
            enabled = False
            i += 7
            continue

        elif file[i:i+4] == "do()":
            enabled = True
            i += 4
            continue

        elif file[i : i + 4] == "mul(":
            if enabled:
                temp = find_mul(i + 4, file)
                if temp is not None:
                    ans += temp
        
        i += 1
    return ans

if __name__ == "__main__":
    res1, res2 = 0, 0
    file = open("input3.txt", "r")

    content = file.read()
    res1 += solve_part1(content)
    res2 += solve_part2(content)
    print(res1)
    print(res2)





'''
import re

# Read input from file
with open("input3.txt", "r") as file:
    input_text = file.read()

# Part 1
def part1():
    regex = r"mul\(\d{1,3},\d{1,3}\)"
    matches = re.findall(regex, input_text)
    

    total = 0
    
    for match in matches:
        a, b = get_numbers(match)
        total += a * b
    
    print(f"Total: {total}")


# Part 2
def part2():
    regex = r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)"
    matches = re.findall(regex, input_text)

    is_enabled = True  # At the start, mul instructions are enabled
    total = 0

    for match in matches:
        if match == "do()":
            is_enabled = True
        elif match == "don't()":
            is_enabled = False
        elif match.startswith("mul") and is_enabled:
            a, b = get_numbers(match)
            total += a * b

    print(f"Total: {total}\n")


# Helper function to extract numbers from a match
def get_numbers(match):
    numbers = re.findall(r"\d{1,3}", match)
    return int(numbers[0]), int(numbers[1])

# Execute parts
part1()
part2()
'''