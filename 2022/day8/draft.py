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
    print(total)
    for row_index in range(len(grid)):
        if row_index > 0 and row_index < (len(grid)-1):
            for col_index in range(len(grid[row_index])):
                if col_index > 0 and col_index < (len(grid[row_index])-1):
                    top = grid[row_index-1][col_index]
                    bottom = grid[row_index+1][col_index]
                    centre = grid[row_index][col_index]
                    left = grid[row_index][col_index-1]
                    right = grid[row_index][col_index+1]
                    if centre > top:
                        row_fig = row_index
                        while row_fig > 0:
                            if grid[row_fig][col_index] > grid[row_fig-1][col_index] and row_fig == 1:
                                total += 1
                                # print('row: ' + str(row_index) + ' col: ' + str(col_index))
                                # print('top')
                                break
                            elif grid[row_fig][col_index] < grid[row_fig-1][col_index]:
                                break
                            else:
                                row_fig -= 1
                    if centre > bottom:
                        row_fig = row_index
                        while row_fig < len(grid)-1:
                            if grid[row_fig][col_index] > grid[row_fig+1][col_index] and row_fig == (len(grid)-2):
                                total += 1
                                # print('row: ' + str(row_index) + ' col: ' + str(col_index))
                                # print('bottom')
                                break
                            elif grid[row_fig][col_index] < grid[row_fig+1][col_index]:
                                break
                            else:
                                row_fig += 1
                    if centre > left:
                        col_fig = col_index 
                        while col_fig > 0:
                            if grid[row_index][col_fig] > grid[row_index][col_fig-1] and col_fig == 1:
                                total += 1
                                # print('row: ' + str(row_index) + ' col: ' + str(col_index))
                                # print('left')
                                break
                            elif grid[row_index][col_fig] < grid[row_index][col_fig-1]:
                                break
                            else:
                                col_fig -= 1
                    if centre > right:
                        col_fig = col_index
                        while col_fig <= len(grid[0])-1:
                            if grid[row_index][col_fig] > grid[row_index][col_fig+1] and col_fig == (len(grid[0])-2):
                                total += 1
                                print('row: ' + str(row_index) + ' col: ' + str(col_index))
                                print('right')
                                break
                            elif grid[row_index][col_fig] < grid[row_index][col_fig+1]:
                                break
                            else:
                                col_fig += 1  
                                




    
    return total

if __name__ == "__main__":
    start_time = timeit.default_timer()
    with open(r'/Users/godfreynelmes/Documents/GitHub/advent-of-code/2022/day8/input8.txt', 'r') as f:
        text = f.read()
    grid = input_cleaner(text)
    print(f'Challenge 1 Answer: {tree_counter(grid)}')
    #print(f'Challenge 2 Answer: {calorie_counter(lines)[1]}')
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))