def basin_count(line_grid):
    dict = {}
    count = 0
    for line_index in range(len(line_grid)):    
        for num_index in range(len(line_grid[line_index])):
            print(count)
            count += 1
            if line_grid[line_index][num_index] != 9:
                new_dict = dict
                for key in dict:
                    #checks the cell below
                    if line_index != (len(line_grid)-1) and (str(line_index+1) + " " + str(num_index)) in dict[key]:
                        new_dict[key].append(str(line_index) + " " + str(num_index))
                    #checks the cell to left
                    elif num_index != 0 and (str(line_index) + " " + str(num_index-1)) in dict[key]:
                        new_dict[key].append(str(line_index) + " " + str(num_index))
                    else:
                        new_dict[len(dict)] = [str(line_index) + " " + str(num_index)]
                if len(dict) == 0:
                    new_dict[0] = [str(line_index) + " " + str(num_index)]
                dict = new_dict
                print(dict)

    print(dict)
    size_list = []
    for key in range(len(dict)):
        size_list.append(len(dict[key]))

    return sum(sorted(size_list)[-3:])