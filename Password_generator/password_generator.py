import random 
import array 


global random_digit
global random_lower
global random_special
global random_upper

def char_pref():
	print("Characters used:\n    For digits press '1'\n    For lowercase characters press '2'\n    For uppercase characters press '3'\n    For all characters press '4'\n    Note *special characters are always included")
	print("############################################################################################################\n")
	print("\n############################################################################################################")
	print("Enter any number of preferences are:")
	password =""
	pref=input()
	if pref == '1':
		mixed_list1 = digits + special
		ranlist = random_digit + random_special
		password = generate_pass(mixed_list1,ranlist)
	elif pref == '2':
		mixed_list1 = lowercase_ch + special
		ranlist = random_lower + random_special
		password = generate_pass(mixed_list1,ranlist)
	elif pref == '3':
		mixed_list1 = uppercase_ch +special
		ranlist = random_upper + random_special
		password = generate_pass(mixed_list1,ranlist)
	elif pref == '4':
		mixed_list1 = digits + uppercase_ch + lowercase_ch + special
		ranlist = random_special + random_digit + random_lower + random_upper
		password = generate_pass(mixed_list1,ranlist)
	return password
	

	
			


def generate_pass(lis,ranlist):
	password = ''
	print("Enter the maximum length")
	maximum_length = int(input())
	temp_pass_list = []
	for _ in range(maximum_length - 4): 
		ranlist = ranlist + random.choice(lis) 
		temp_pass_list = array.array('u', lis) 
		random.shuffle(temp_pass_list)
		
	for i in range(maximum_length): 
		password = password + temp_pass_list[i]
		
    
	return password
# maximum length of password needed 

# creating list of available characters
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
lowercase_ch = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z'] 

uppercase_ch = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z'] 

special = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<'] 


random_digit = random.choice(digits) 
random_upper = random.choice(uppercase_ch) 
random_lower = random.choice(lowercase_ch) 
random_special = random.choice(special) 

global password
password = "" 
flag= True
# print out password 
password = char_pref()
print(password)

while (flag):
	print("Want to proceed ? (y/n)")
	choice = input()
	if choice == 'y':
		password = char_pref()
		print(password)
	else :
		flag = False
