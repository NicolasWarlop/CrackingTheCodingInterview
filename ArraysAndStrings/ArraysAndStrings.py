import re

#ArraysAndStrings example
#1.1 Implement an algorithm to determine is a string has all unique characters. What if you cannot use additional data structures?

def isUnique(testString):
	if len(testString) < 2:
		return True

	testString = sorted(testString)
	#If we cannot use any other data structure, sort the list, and compare each index with the successive one.
	for i in range(len(testString) - 1):
		if testString[i] == testString[i+1]:
			return False
	return True

# test1 = 'ACBDBAQR' #duplicate A
# test2 = 'ABCDEFG' #no duplicate values
# test3 = 'A' #1 character
# test4 = '' #empty string

#print(isUnique(test1),isUnique(test2),isUnique(test3),isUnique(test4))

#1.2 Given two strings, write a method to decide if one is a permutation of the other

def isPermutation(string1, string2):
	if len(string1) != len(string2):
		return False

	string1 = ''.join(sorted(string1))
	string2 = ''.join(sorted(string2))

	if string1 == string2:
		return True
	else:
		return False

# test1a, test1b = 'ABCABC', 'AABBCC' #Strings are permutations of one another (expected true)
# test2a, test2b = 'ABCABC', 'ABCABD' #Strings are not permutations of one another (expected false)
# test3a, test3b = 'AB?CABÉ', 'AB?ÉABC' #Matching special characters? (expected true)
# test4a, test4b = 'EEEEE', 'EEÉEE' #Matching special characters? (expected false)
# test5a, test5b = '12345', '1234' #Should be completed without sorting (expected false)

# print(isPermutation(test1a,test1b),isPermutation(test2a,test2b),isPermutation(test3a,test3b),isPermutation(test4a,test4b), isPermutation(test5a,test5b))

#1.3 Write a method to replace all spaces in a string with '%20'

def URLIfy(testString):
	testString = list(testString)

	for i in range(len(testString)):
		if testString[i] == ' ':
			testString[i] = '%20'
	return ''.join(testString)

# test1 = 'A simple example'
# test2 = 'An example with a tab	.'
# test3 = 'An example with a newline \n included'
# test4 = 'An  example  with  double  spaces'

# print(URLIfy(test1))
# print(URLIfy(test2))
# print(URLIfy(test3))
# print(URLIfy(test4))

#1.4 Palindrome validator
def getCharCounts(string1):
	dictionnary = {}

	for i in range(len(string1)):
			if string1[i] in dictionnary:
				dictionnary[string1[i]] += 1
			else:
				dictionnary[string1[i]] = 1
	return dictionnary

def isPalPermutation(string1):
	#assume we ignore non-alphanumeric characters
	#We'll ignore case
	mydict = {}
	string1 = re.sub(r'\W+','', string1)

	if len(string1) % 2 == 0:
		#Even number of characters. all characters must have a matching pair
		mydict = getCharCounts(string1)

		for elem in mydict:
			if mydict[elem] % 2 != 0:
				return False

		return True
	else:
		#Odd number of characters. Similar logic to that above, except for the 1 "allowed" discrepancy
		mydict = getCharCounts(string1)

		counter = 0
		for elem in mydict:
			if mydict[elem] % 2 != 0:
				counter += 1
				if counter > 1:
					return False

		return True

# test1 =  'TACO CAT' #odd palindrome
# test2 = 'TACO CATO' #even palindrome
# test3 = 'TACOL CART' #Not a palindrome
# test4 = 'ACTO ACTB' #Not a palindrome

# print(isPalPermutation(test1))
# print(isPalPermutation(test2))
# print(isPalPermutation(test3))
# print(isPalPermutation(test4))

#1.5 One Away
def isOneAwayMod(string1,string2):
	counter = 0
	for i in range(len(string1)):
		if string1[i] != string2[i]:
			counter += 1
			if counter > 1:
				return False
	return True


def isOneAwayAdd(string1,string2):
	#string 2 must be the larger string
	counter = 0
	string1, string2 = list(string1), list(string2)
	for i in range(len(string1)):
		if string1[i] != string2[i]:
			#We have found the alleged insertion. Remove the element from string2 and re-evaluate
			counter += 1
			del string2[i]
			if string1[i] != string2[i]:
				return False
			if counter > 1:
				return False
	return True

def isOneAway(string1,string2):
	if len(string1) == len(string2):
		#Can only be a modification
		return isOneAwayMod(string1,string2)
	elif abs(len(string1) - len(string2)) > 1:
		return False
	elif len(string1) < len(string2):
		return isOneAwayAdd(string1, string2)
	else:
		#Removal is the same comparison as insertion, with the strings inverted
		return isOneAwayAdd(string2, string1)

# test1a, test1b = 'POLE', 'POKE' #Mod pass
# print(isOneAway(test1a,test1b))
# test2a, test2b = 'POLE', 'POKD' #Mod fail
# print(isOneAway(test2a,test2b))
# test3a, test3b = 'POLE', 'POKESS' #Length fail
# print(isOneAway(test3a,test3b))
# test4a, test4b = 'POLE', 'POLES' #Add pass
# print(isOneAway(test4a,test4b))
# test5a, test5b = 'POLE', 'PALES' #Add fail
# print(isOneAway(test5a,test5b))
# test6a, test6b = 'POLE', 'PLE' #Sub pass
# print(isOneAway(test6a,test6b))
# test7a, test7b = 'POLE', 'PAL' #Sub fail
# print(isOneAway(test7a,test7b))

#1.6 String Compression


def compressString(string1):
	retStr = ''
	curridx = 0
	count = 1

	if re.search(r"(\w+)\1", string1) is None:
		return string1
	else:
		while True:
			try:
				if string1[curridx] == string1[curridx+1]:
					count += 1
				else:
					retStr += string1[curridx] + str(count)
					count = 1
				curridx += 1
			except:
				#reached the end of the string. Add on the final value
				retStr += string1[curridx] + str(count)
				break
		
	return retStr

# test1 = 'abcdefg' #No duplicates, return the same string
# print(compressString(test1))
# test2 = 'aaaabbbbcddddefgggg'
# print(compressString(test2))
# test3 = 'aaaabbbbcddddefg'
# print(compressString(test3))

#1.7 Rotate Matrix

def rotateMatrix(matrix):
	#we know we have an nxn matrix

test = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
