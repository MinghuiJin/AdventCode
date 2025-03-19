def parse_file(file_name):
    file = open(file_name, "r")
    rules = {}
    updates = []
    found_section = False
    for line in file.readlines():
        if line == '\n':
            found_section = True
            continue

        if not found_section:
            x, y = line.strip('\n').split('|')
            if x not in rules:
                rules[x] = []
            rules[x].append(y)
        else:
            l = line.strip('\n').split(',')
            updates.append(l)
    
    return rules, updates
    

def is_valid_update(update, rules):
    for i in range(1, len(update)):
        if update[i - 1] not in rules or update[i] not in rules[update[i - 1]]:
            return False    
    return True

def solve_part_1(rules, updates):
    ans = 0
    for update in updates:
        if is_valid_update(update, rules):
            mid = update[len(update) // 2]
            ans += int(mid)
    print(ans)
    return ans
        
def solve_part_2(rules, updates):
    ans = 0
    for update in updates:
        if not is_valid_update(update, rules):
            for idx in range(1, len(update)):
                i = idx
                while i > 0:
                    if update[i - 1] not in rules or update[i] not in rules[update[i - 1]]:
                        update[i - 1], update[i] = update[i], update[i - 1]
                        i -= 1
                    else: 
                        break
            ans += int(update[len(update) // 2])
    print(ans)
    return ans

if __name__ == "__main__":
    rules, updates = parse_file("input5.txt")
    # solve_part_1(rules, updates)
    solve_part_2(rules, updates)