dirs = {'up': (0, -1), 'down': (0, 1), 'left': (-1, 0), 'right': (1, 0), 'up-left': (-1, -1), 'up-right': (-1, 1), 'down-left': (1, -1), 'down-right': (1, 1)}

def find_word(puzzle):
    all_X =  []
    ans = 0
    for r in range(len(puzzle)):
        for c in range(len(puzzle[0])):
            if puzzle[r][c] == 'X':
                all_X.append((r, c))
    
    for r, c in all_X:
        for x, y in dirs.values():
            if 0 <= r + x * 3 < len(puzzle) and 0 <= c + y * 3 < len(puzzle[0]):
                if puzzle[r][c] + "" + puzzle[r + x][c + y] + "" + puzzle[r + x * 2][c + y * 2] + "" + puzzle[r + x * 3][c + y * 3] == 'XMAS':
                    ans += 1
    print(ans)

def find_X_MAS(puzzle):
    all_A = []
    for r in range(1, len(puzzle) - 1):
        for c in range(1, len(puzzle[0]) - 1):
            if puzzle[r][c] == 'A':
                all_A.append((r, c))
    
    ans = []
    for r, c in all_A:
        if puzzle[r - 1][c - 1] != puzzle[r + 1][c + 1] and puzzle[r - 1][c - 1] in 'MS' and puzzle[r + 1][c + 1] in 'MS':
            if puzzle[r - 1][c - 1] == puzzle[r + 1][c - 1] and puzzle[r - 1][c + 1] == puzzle[r + 1][c + 1] or puzzle[r - 1][c - 1] == puzzle[r - 1][c + 1] and puzzle[r + 1][c + 1] == puzzle[r + 1][c - 1]:
                ans.append((r, c))
    
    print(len(ans))
            


if __name__ == "__main__":
    puzzle = []
    file = open("input4.txt", "r")
    lines = file.readlines()
    for line in lines:
        puzzle.append(list(line.strip('\n')))

    # find_word(puzzle)
    find_X_MAS(puzzle)

