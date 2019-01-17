def checkPermutationBySort(S,T):
	if len(S) != len(T):
		return False

	return sorted(S) == sorted(T)

print(checkPermutationBySort('abcdef','fedcba'))