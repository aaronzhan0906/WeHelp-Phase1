def find(spaces, stat, n):
    for i in range(len(spaces)):
        if stat[i] == 0:
            spaces[i] = 0
    
    min_space_index = -1
    min_difference = float('inf')

    for i in range(len(spaces)):
        difference = spaces[i] - n

        if difference >= 0 and difference < min_difference:
            min_difference = difference
            min_space_index = i

    print(min_space_index)


find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2) # print 5
find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) # print -1
find([4, 6, 5, 8], [0, 1, 1, 1], 4) # print 2