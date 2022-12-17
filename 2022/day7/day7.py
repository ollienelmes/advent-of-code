import timeit

def input_cleaner(text):
    lines = text.split('\n')

    return lines

def dir_nav(lines):
    file_dict = {}
    current_address = []
    for line in lines:
        #Changing directory and making a note of current address
        if line == '$ cd /':
            current_address.append(line.split('cd ')[1])
        elif '$ cd' in line and '..' not in line:
            current_address.append(line.split('cd ')[1]+'/')
        elif '..' in line:
            current_address.pop()

        #listing protocool
        if '$' not in line and 'dir' not in line:
            if ''.join(current_address) not in file_dict:
                file_dict[''.join(current_address)] = int(line.split(' ')[0])
            elif ''.join(current_address) in file_dict:
                file_dict[''.join(current_address)] += int(line.split(' ')[0])
    
    
    new_file_dict = {}
    for x in file_dict.keys():
        if x == '/':
            new_file_dict[x] = file_dict[x]
        else:
            new_file_dict[x[:-1]] = file_dict[x]
    
    #print(new_file_dict)
    total = 0
    total_file_dict = {}
    for address in new_file_dict.keys():
        address_list = address.split('/')
        new_add = ''
        #we don't want the total root
        if address_list != ['','']:
            for dir in address_list:
                if dir == '':
                    new_add = '/'
                    total_file_dict[new_add] += new_file_dict[address]
                else:
                    new_add += dir + '/'
                    if new_add not in total_file_dict:
                        total_file_dict[new_add] = new_file_dict[address]
                    else:
                        total_file_dict[new_add] += new_file_dict[address]

                #print(new_add)
        else:
            total_file_dict['/'] = new_file_dict[address]

    #print(total_file_dict)

    for x in total_file_dict.values():
        if x < 100000:
            total += x

    total_space = total_file_dict['/']
    free_space = 70000000 - total_space
    min_deletion = 30000000 - free_space
    
    deletion_list = []
    for x in total_file_dict.values():
        if x >= min_deletion:
            deletion_list.append(x)

    return total, min(deletion_list)


    

if __name__ == "__main__":
    start_time = timeit.default_timer()
    with open(r'/Users/godfreynelmes/Documents/GitHub/advent-of-code/2022/day7/input7.txt', 'r') as f:
        text = f.read()
    lines = input_cleaner(text)
    print(f'Challenge 1 Answer: {dir_nav(lines)[0]}')
    print(f'Challenge 2 Answer: {dir_nav(lines)[1]}')
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))