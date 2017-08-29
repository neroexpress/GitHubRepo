'''
Code developed by - Narender Kumar
This code requires Python 3.0, and for other versions, the code will not compile.
Please make sure that all the required contstraints are met in the input text file,
the code will not check for the required constraints. That is 1 ≤ N ≤ 200,000 days 
and 1 ≤ K ≤ N days.
This code creates an output text file(output.txt), in the same directory as this program.
'''

# The code starts from here

input_file_name = "input.txt"
output_file_name = "ouput.txt"

def read_text_file(fn):
	'''
	This function reads the text file and stores the N value and K value in data structure.
	This function also stores the sale price from the input text file
	'''
	with open(fn) as f:
		read_data = f.readlines()
	i=1
	N_values = list()
	for x in read_data:
		if i==1:
			K_values = [int(y) for y in x.split()]
			i+=1
		else:
			x = [int(x) for x in x.split()]
			N_values.extend(x)
	return K_values,N_values

def number_of_increasing_Subranges(window):
	'''
	This function returns the number of increasing subranges.
	'''
	increasing_subrange = 0
	for j in range(len(window)-1):
		for i in range(len(window)-1):
			new_window = window[j:len(window)-i]
			if len(new_window)<2:continue
			if all(new_window[p] < new_window[p+1] for p in range(len(new_window)-1)):
				increasing_subrange +=1
	return increasing_subrange

def number_of_decreasing_Subranges(window):
	'''
	This function returns the number of decreasing subranges.
	'''
	decreasing_subrange = 0
	for j in range(len(window)-1):
		for i in range(len(window)-1):
			new_window = window[j:len(window)-i]
			if len(new_window)<2:continue
			if all(new_window[p] > new_window[p+1] for p in range(len(new_window)-1)):
				decreasing_subrange +=1
	return decreasing_subrange

def do_computation(k,n_list):
	'''
	This function returns a list of increasing subranges within 
	the window minus the number of decreasing subranges within the window.
	'''
	j = 0
	computed_list = list()
	for x in range(k[0]- k[1]+1):
		num_inc = number_of_increasing_Subranges(n_list[j:k[1]+j])
		num_dec = number_of_decreasing_Subranges(n_list[j:k[1]+j])
		j+=1
		#print(num_inc-num_dec)
		computed_list.append(num_inc-num_dec)
	return computed_list

def print_to_textfile(fn,list_of_values):
	'''
	This function prints the answer to a output text file as well to the consol.
	'''
	with open(fn,'wt') as f:
		for s in list_of_values:
			print(s)
			print(s, file=f)

K_values,N_values = read_text_file(input_file_name)
print_to_textfile(output_file_name,do_computation(K_values,N_values))

#End of code



