#Opening input.txt file and appending each lines in lst list
lst = open("input.txt").read().splitlines()

# Function that compare two strings and return number of difference between them
def diff_letters(a,b):
    return sum ( a[i] != b[i] for i in range(len(a)) )

# Main function that compare all the strings in lst until it finds only one diffenrence between two strings, then break to avoid unnecessary comparaisons
def boxesCheck():
	i = 0
	y = 1
	while i < len(lst):
		while y < len(lst):
			count = diff_letters(lst[i],lst[y]) 
			if count == 1:
				print("les boites contenant le robot sont les numeros",i+1,"et",y+1,)
				break
			y+=1
		i+=1
		y = i + 1

boxesCheck()

#lst.close()

