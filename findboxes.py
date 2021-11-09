#Opening input.txt file and appending each lines in lst list
lst = open("input.txt").read().splitlines()

# Function that compare two strings and return number of difference between them
def diffLetters(a,b):
    return sum ( a[i] != b[i] for i in range(len(a)) )

# Function that take two strings in parameters and compare them to get the common letters
def commonLetters(lst1,lst2):
	i = 0
	res = ""
	while i < len(lst1):
		if lst1[i] == lst2[i]:
			res+=lst1[i]
		i+=1
	return res

# Main function that compare all the strings in lst until it finds only one diffenrence between two strings, then break to avoid unnecessary comparaisons
def boxesCheck():
	i = 0
	y = 1
	while i < len(lst):
		while y < len(lst):
			count = diffLetters(lst[i],lst[y]) 
			if count == 1:
				print("according there is no box nb 0, the boxes that contain the robot's part are box nb",i+1,"and",y+1,)
				res = commonLetters(lst[i],lst[y])
				print("common letter between the two boxes are :",res)
				break
			y+=1
		i+=1
		y = i + 1

boxesCheck()
