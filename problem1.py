

def count_sizes(data):
    num_tri = 0
    shared = 0

    for r in range(2):
        for c in range(len(data[r])):
                if data[r][c] == 1:
                    if c < len(data[r]) - 1 and data[r][c + 1] == 1:
                        shared += 1

                    if r == 0 and c % 2 == 0 and data[r + 1][c] == 1 :
                        shared += 1
                    
                    num_tri += 1

    #print(num_tri, shared, num_tri * 3 - shared * 2)
    return num_tri * 3 - shared * 2


data1 = [
    [0, 1, 1, 0, 1, 1, 1, 0, 0], 
    [0, 1, 0, 1, 0, 1, 1, 0, 0]
]

data2 = [
    [1, 0, 1, 0, 1], 
    [0, 0, 0, 0, 0]
]

data3 = [
    [0, 0, 1, 1, 0, 1, 0], 
    [0, 0, 1, 0, 1, 0, 0]
]

print(count_sizes(data1))
print(count_sizes(data2))
print(count_sizes(data3))
