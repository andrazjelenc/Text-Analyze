
def getOccurance(ListOfWords):
	Concatenated = ''.join(ListOfWords)
	UniqueChars = set(Concatenated)
	List = []
	for Char in UniqueChars:
		List.append([Char, Concatenated.count(Char)])
	return List
	
def toPercentages(List):
	TotalChars = sum([x[1] for x in List])
	return [[x[0], round(x[1]*100 / float(TotalChars), 3)] for x in List]


def sortByOccurance(List):
	return sorted(List, key=lambda x: x[1], reverse=True)

	
def sortByAlphabet(List):
	return sorted(List, key=lambda x: x[0])
