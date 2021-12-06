import timeit

def input_loader(text):
    input_array = text.split("\n\n")
    input_list = input_array[0]
    bingo_grid = input_array[1:]
    bingo_out = []
    bingo_nums = []
   
    for bingo in bingo_grid:
        grid = bingo.split("\n")
        bingo_out.append(grid)
    
    for list in bingo_out:
        bingo_box = []
        for row in list:  
            nums = row.split(" ")
            int_nums = []
            for num in nums:
                if len(num) != 0:
                    int_nums.append(int(num))
            bingo_box.append(int_nums)
            
        bingo_nums.append(bingo_box)
        
    called_list = input_list.split(",")
    #print(bingo_nums)
    return called_list, bingo_nums

def checker (bingo):
    #checks rows
    for grid in bingo:
        for row in grid:
            if sum(row) == -5:
                grid_total = 0
                for row in grid:
                    for num in row:
                        if num != -1:
                            grid_total += int(num)
                return True, grid_total, bingo.index(grid)
                         
    #checks columns
    for grid in bingo:
        for column_index in range(0,5):
            column_total = grid[0][column_index] + grid[1][column_index] + grid[2][column_index] + grid[3][column_index] + grid[4][column_index]
            if column_total == -5:
                grid_total = 0
                for row in grid:
                    for num in row:
                        if num != -1:
                            grid_total += int(num)
                return True, grid_total, bingo.index(grid)
    
    return False, 0, 0

def challenge_1 (input_list, bingo):
    new_bingo = bingo
    for called_num in input_list:
        bingo = new_bingo
        new_bingo = []
        for grid in bingo:
            new_grid = []
            for row in grid:
                new_row = []
                for num in row: 
                    #print(num)
                    if int(num) == int(called_num):
                        new_row.append(-1)
                    else:
                        new_row.append(num)
                new_grid.append(new_row)
            new_bingo.append(new_grid)
        
        bingo_check, grid_sum, grid_index = checker(new_bingo)
        
        if bingo_check == True:
            return grid_sum * int(called_num)
 

    return False

def challenge_2 (input_list, bingo):
    new_bingo = bingo
    for called_num in input_list:
        bingo = new_bingo
        new_bingo = []
        for grid in bingo:
            new_grid = []
            for row in grid:
                new_row = []
                for num in row: 
                    #print(num)
                    if int(num) == int(called_num):
                        new_row.append(-1)
                    else:
                        new_row.append(num)
                new_grid.append(new_row)
            new_bingo.append(new_grid)
        
            bingo_check, grid_sum, grid_index = checker(new_bingo)
        
            if bingo_check == True:
                last_called_num = int(called_num)
                last_grid_sum = grid_sum
                print('last called num: ' + str(last_called_num))
                print('last sum: ' + str(last_grid_sum))
                print(len(new_bingo))
                new_bingo.pop(grid_index)


    return last_called_num * last_grid_sum



if __name__ == "__main__":
    start_time = timeit.default_timer()
    with open(r'input4.txt', 'r') as f:
        text = f.read()
    input_list, bingo = input_loader(text)
    print(f'Challenge 1 Answer: {challenge_1(input_list, bingo)}')
    print(f'Challenge 2 Answer: {challenge_2(input_list, bingo)}')
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))