
input = """
XZASLKDJF
SDFJGGIOG
XLFGFOIRC
VVLFGLGKK
BKBKFJDJG
LSLFKFKFK
BKHJHLKIV
VKXKXUWPW
BJJXJHWPX
"""

def test_word(data, word, row, col, row_dir, col_dir, color):
    size = len(word)
    rows = len(data)
    cols = len(data[0])

    if row_dir > 0 and row + size > rows:
        return False
    
    if row_dir < 0 and row + 1 - size < 0:
        return False

    if col_dir > 0 and col + size > cols:
        return False

    if col_dir < 0 and col + 1 - size < 0:
        return False
    
    for x in range(size):
        if data[row + x * row_dir][col + x * col_dir] != word[x]:
            return False

    for x in range(size):
        color[row + x * row_dir][col + x * col_dir] = 1

    return True

def search_word(input, word):
    data = []
    for row in input.split('\n'):
        if len(row) > 0:
            data.append(list(row))

    color = []
    for y in data:
        color.append([0] * len(y))

    count = 0
    x = len(word)
    h = len(data)
    for r in range(h):
        w = len(data[r])
        for c in range(w):
            for col_dir in [-1, 0, 1]:
                for row_dir in [-1, 0, 1]:
                    if col_dir == 0 and row_dir == 0:
                        continue
                    else:
                        if test_word(data, word, r, c, row_dir, col_dir, color):
                            count += 1
    
    for r in range(h):
        for c in range(len(data[r])):
            if color[r][c] == 1:
                print(f"\033[92m{data[r][c]}\033[0m", end='')
            else:
                print(f"{data[r][c]}", end='')

        print()

    return count


print("--------------------")
found = search_word(input, "JK")
print("--------------------")
print(f"Found {found} occurrence(s)")
