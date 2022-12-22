import re
password = input("enter your password: ")
flag = 0
while True:
		
	if not re.search("[a-z]", password):
		flag = -1
	
	elif not re.search("[A-Z]", password):
		flag = -1
		
	elif not re.search("[0-9]", password):
		flag = -1
		
	elif not re.search("[_@$]", password):
		flag = -1
	
	elif (len(password)<8):
        	print("invalid")
        	break
	
	elif (len(password)>16):
        	print("invalid")
        	break


if flag == 0:
	print("Strong strength password and valid")
elif flag == -1:
	print("Medium strength password and valid")
elif flag == -2:
	print("Medium strength password and valid")
elif flag == -3:
	print("Weak password and invalid")
else:
	print("segmentation fault")

