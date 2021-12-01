with open(r'input.txt', 'r') as f:
    text = f.read()

data_list = text.split('\n')
depth_counter = 0
previous_val = data_list[0]
output_string = ""
for x in data_list:
    if int(x) > int(previous_val):
        depth_counter += 1
    previous_val = x

print(depth_counter)



content_list = [int(item) for item in data_list]

i = 0  
three_sum_list = []
for i in range(len(data_list) - 2):
    current_sum = content_list[i] + content_list[i+1] + content_list[i + 2]
    three_sum_list.append(current_sum)
    

depth_counter_sum = 0
previous_val_sum = three_sum_list[0]

for y in three_sum_list:
    if int(y) > int(previous_val_sum):
        depth_counter_sum += 1
    previous_val_sum = y

print(depth_counter_sum)
