import timeit

def input_cleaner(text):
    lines = text.split("\n")
    line_grid = []
    for line in lines:
        line_list = []
        for num in line:
            line_list.append(int(num))
        line_grid.append(line_list)

    return line_grid

def flash_counter(grid):
    #reference table
    #left = grid[column_index][row_index-1]
    #right = grid[column_index][row_index+1]
    #up = grid[column_index-1][row_index]
    #down = grid[column_index+1][row_index]
    #up-left = grid[column_index-1][row_index-1]
    #up-right = grid[column_index-1][row_index+1]
    #down-left = grid[column_index+1][row_index-1]
    #down-right = grid[column_index+1][row_index+1]
    
    flash_counter = 0
    flash_counter_list = []

    #increase count on all by one
    for i in range(1000):
        for column_index in range(len(grid)):
            for row_index in range(len(grid[0])):
                grid[column_index][row_index] += 1
        
        #print("increment #" + str(i) + ": " + str(any(10 in sublist for sublist in grid)))
        
        #works through the chain of reactions
        while any(10 in sublist for sublist in grid) or any(11 in sublist for sublist in grid) or any(12 in sublist for sublist in grid) or any(13 in sublist for sublist in grid) or any(14 in sublist for sublist in grid):
            for column_index in range(len(grid)):
                for row_index in range(len(grid[0])):
                    if isinstance(grid[column_index][row_index], int):
                        if grid[column_index][row_index] > 9:
                            flash_counter += 1
                            if row_index != 0: #left
                                if isinstance(grid[column_index][row_index-1], int):
                                    grid[column_index][row_index-1] += 1
                                if column_index != 0: #up-left
                                    if isinstance(grid[column_index-1][row_index-1], int):
                                        grid[column_index-1][row_index-1] += 1
                                if column_index != len(grid) - 1: #down-left
                                    if isinstance(grid[column_index+1][row_index-1], int):
                                        grid[column_index+1][row_index-1] += 1
                            if row_index != len(grid[0]) -1: #right
                                if isinstance(grid[column_index][row_index+1], int):
                                    grid[column_index][row_index+1] += 1
                                if column_index != 0: #up-right
                                    if isinstance(grid[column_index-1][row_index+1], int):
                                        grid[column_index-1][row_index+1] += 1
                                if column_index != len(grid) - 1: #down-right
                                    if isinstance(grid[column_index+1][row_index+1], int):
                                        grid[column_index+1][row_index+1] += 1
                            if column_index != 0: #up
                                if isinstance(grid[column_index-1][row_index], int):
                                    grid[column_index-1][row_index] += 1
                            if column_index != len(grid) - 1: #down
                                if isinstance(grid[column_index+1][row_index], int):
                                    grid[column_index+1][row_index] += 1
                        

                            grid[column_index][row_index] = 'FLASH'
            #print(grid)
            #print(any(10 in sublist for sublist in grid))
            #print(str(flash_counter) + " " +  str(i))
        
        #tidy up the grid, reset certain numbers to 0 
        set_of_nums = []
        for column_index in range(len(grid)):
            for row_index in range(len(grid[0])):
                if grid[column_index][row_index] == 'FLASH':
                    grid[column_index][row_index] = 0
                if grid[column_index][row_index] not in set_of_nums:
                    set_of_nums.append(grid[column_index][row_index])

        #print(i)
        #print(grid)
        flash_counter_list.append(flash_counter)

        if set_of_nums == [0]:
            step_number = i + 1
            break
    return flash_counter_list[99], step_number


if __name__ == "__main__":
    start_time = timeit.default_timer()
    with open(r'input11.txt', 'r') as f:
        text = f.read()
    grid = input_cleaner(text)
    counter, full_flash = flash_counter(grid)
    print(f'Challenge 1 Answer: {counter}')
    print(f'Challenge 2 Answer: {full_flash}')
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))