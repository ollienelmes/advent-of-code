opening = ['{','[','(','<']
li = ['{','[','(',']']
end_points = ['\{\}','[]','()','<>']

if set(li) <= set(opening):
	print('yes')
else:
	print('no')


test = "<{([([[(){}]>(<<{{"

for pair in end_points:



            set_of_chars = set([char for char in line2])
            print(set_of_chars)
            if set_of_chars <= set(opening_list):
                break
            else:
            #create a regex which tests if there are any endpoints in the line, if false then we can take the first one in the closers group below, if true then continue with the loop    
            for pair in end_points:
                if pair not in line2:
                    print(line2)
                    closers = list(set_of_chars - set(opening_list))
                    illegal_chars.append(closers[0])
                    line2 = ""
                    break
re = '[\[\]]+ '