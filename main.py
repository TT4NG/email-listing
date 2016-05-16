def main():
	string = input("Please enter a valid email address with the format name@blank.com: ")
	email = string.split("@")
	list = [email[0],email[1]]
	TLD = email[1].split(".")
	list2 = [TLD[0],TLD[1]]
	if email[0].isalpha():
		print ("name is: ",list[0])
		print ("url is:  ",list2[0])
		print ("TLD is:  ", list2[1])
	else:
		print("invalid email address")
		return False
main()