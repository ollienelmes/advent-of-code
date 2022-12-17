import timeit

def input_cleaner(text):
    lines = text.split('\n')
    grid= []
    for line in lines:
        working_line = []
        for num in line:
            working_line.append(int(num))
        grid.append(working_line)
    return grid

def tree_counter(grid):
    total = (2*len(grid)) + (2*len(grid[0])) - 4 
    score_list = []
    for row_index in range(len(grid)):
        if row_index > 0 and row_index < (len(grid)-1):
            for col_index in range(len(grid[row_index])):
                if col_index > 0 and col_index < (len(grid[row_index])-1):
                    centre = grid[row_index][col_index]
                    
                    top_list = []
                    bottom_list = []
                    left_list = []
                    right_list = []

                    top_i = row_index
                    bottom_i = row_index
                    left_i = col_index
                    right_i = col_index

                    while top_i > 0:
                        top_i -= 1
                        top_list.append(grid[top_i][col_index])
                    
                    while bottom_i < len(grid) - 1:
                        bottom_i += 1
                        bottom_list.append(grid[bottom_i][col_index])

                    while left_i > 0:
                        left_i -= 1
                        left_list.append(grid[row_index][left_i])

                    while right_i < len(grid[0]) - 1:
                        right_i += 1
                        right_list.append(grid[row_index][right_i])

                    if centre > max(top_list) or centre > max(bottom_list) or centre > max(left_list) or centre > max(right_list):
                        total += 1

                    top_score = 0
                    bottom_score = 0
                    left_score = 0
                    right_score = 0

                    for tree in top_list:
                        top_score += 1
                        if tree < centre:
                            pass
                        else:
                            break
                    for tree in bottom_list:
                        bottom_score += 1
                        if tree < centre:
                            pass
                        else:
                            break
                    for tree in left_list:
                        left_score += 1
                        if tree < centre:
                            pass
                        else:
                            break
                    for tree in right_list:
                        right_score += 1
                        if tree < centre:
                            pass
                        else:
                            break                          
                    
                    #print(str(top_score) + ' * ' + str(bottom_score) + ' * ' + str(left_score) + ' * ' + str(right_score) )
                    score_list.append(top_score*bottom_score*left_score*right_score)

                     
    return total, max(score_list)

if __name__ == "__main__":
    start_time = timeit.default_timer()
    with open(r'/Users/godfreynelmes/Documents/GitHub/advent-of-code/2022/day8/input8.txt', 'r') as f:
        text = f.read()
    grid = input_cleaner(text)
    print(f'Challenge 1 Answer: {tree_counter(grid)[0]}')
    print(f'Challenge 2 Answer: {tree_counter(grid)[1]}')
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))