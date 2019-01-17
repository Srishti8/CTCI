#Is Unique

def isUnique(S):
	if not S:
		return

	hashTable = []

	for i in S:
		if i in hashTable:
			return False
		else:
			hashTable.append(i)


	return True

print(isUnique('abcdea'))
