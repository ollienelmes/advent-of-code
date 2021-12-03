import timeit
def bit_counter(bit_list):
    bit_dict = {}
    for i in range(12):
        bit_dict[i] = 0

    for x in bit_list:
        for i in range(0, len(x)):
            if x[i] == '1':
                bit_dict[i] += 1
            elif x[i] == '0':
                bit_dict[i] -= 1
    return bit_dict

def power_consumption(bit_list):
    gamma_rate = ""
    epsilon_rate = ""
    bit_dict = bit_counter(bit_list)
    for x in range(0, len(bit_dict)):
        if bit_dict[x] > 0:
            gamma_rate += '1'
            epsilon_rate += '0'
        else:
            gamma_rate += '0'
            epsilon_rate += '1'      
    
    return int(gamma_rate, 2) * int(epsilon_rate, 2)

def life_support(bit_list):
    oxygen_rating = ""
    co_scrubber = ""
    index = 0
    bit_list_copy = bit_list
    while index < len(bit_list[0]):
        if len(bit_list) == 1:
            oxygen_rating += bit_list[0]
        bit_dict = bit_counter(bit_list)
        if bit_dict[index] >= 0:
            new_list = [bit for bit in bit_list if bit[index] != '0']
            bit_list = new_list
        elif bit_dict[index] < 0:
            new_list = [bit for bit in bit_list if bit[index] != '1']
            bit_list = new_list
        index +=1 

    bit_list = bit_list_copy
    for index in range(len(bit_list[0])):
        if len(bit_list) == 1:
            co_scrubber += bit_list[0]
        bit_dict = bit_counter(bit_list)
        if bit_dict[index] >= 0:
            new_list = [bit for bit in bit_list if bit[index] != '1']
            bit_list = new_list
        elif bit_dict[index] < 0:
            new_list = [bit for bit in bit_list if bit[index] != '0']
            bit_list = new_list
        index +=1 
    return int(co_scrubber, 2) * int(oxygen_rating, 2)

if __name__ == "__main__":
    start_time = timeit.default_timer()
    with open(r'input3.txt', 'r') as f:
        text = f.read()
    bit_list = text.split("\n")
    print(f'Challenge 1 Answer: {power_consumption(bit_list)}')
    print(f'Challenge 2 Answer: {life_support(bit_list)}')
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))