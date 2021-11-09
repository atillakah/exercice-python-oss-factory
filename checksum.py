# Opening file inpute.txt and appending each lines in lst list
lst = open("input.txt").read().splitlines()

# Main function that store in variables and multiplie the number of item in array that contain a letter which appears exactly twice by the number of item where a letter appears exactly three times to get the checksum
def checkSum():
	i = 0
	p = 0
	q = 0
	while i < len(lst):
		res = countOccurences(lst[i])
		if res == 5:
			q+=1
			p+=1
		if res == 3:
			q+=1
		if res == 2:
			p+=1
		i+=1
	print("checksum value is",p*q)

# Function that count number of charactere in given string and can return 3 differents results
def countOccurences(lst):
	i = 0
	res = 0
	char = "abcdefghijklmnopqrstuvwxyz"
	while i < len(char):
		if lst.count(char[i]) == 3:
			res+=3
			break
		i+=1
	i = 0
	while i < len(char):
		if lst.count(char[i]) == 2:
			res+=2
			break
		i+=1
	return res

checkSum()
