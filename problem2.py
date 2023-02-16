
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
            # Test W
            if c <= w - x:
                found = True
                for l in range(x):
                    if data[r][c + l] != word[l]:
                        found = False
                        break
                if found:
                    count += 1
                    for l in range(x):
                        color[r][c + l] = 1
            # Test S
            if r <= h - x:
                found = True
                for l in range(x):
                    if data[r + l][c] != word[l]:
                        found = False
                        break
                if found:
                    count += 1
                    for l in range(x):
                        color[r + l][c] = 1
            # Test E
            if c + 1 >= x:
                found = True
                for l in range(x):
                    if data[r][c - l] != word[l]:
                        found = False
                        break
                if found:
                    count += 1
                    for l in range(x):
                        color[r][c - l] = 1
            # Test N
            if r + 1 >= x:
                found = True
                for l in range(x):
                    if data[r - l][c] != word[l]:
                        found = False
                        break
                if found:
                    count += 1
                    for l in range(x):
                        color[r - l][c] = 1

    
    for r in range(h):
        for c in range(len(data[r])):
            if color[r][c] == 1:
                print(f"\033[92m{data[r][c]}\033[0m", end='')
            else:
                print(f"{data[r][c]}", end='')

        print()

    return count


found = search_word(input, "KGK")

print("Found ", found, " occurrence(s)")
