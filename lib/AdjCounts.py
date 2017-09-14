import itertools

SPACE = '_NL'
MATRIX_DELIMETER = '\t'
MATRIX_NEWLINE = '\r\n'

def getCounts(ListOfWords):
	Concatenated = ''.join(ListOfWords)
	UniqueChars = set(Concatenated)
	# Add space symbol
	UniqueChars.add(SPACE)
	
	AllPairs = set(itertools.product(UniqueChars, repeat=2))
	Counts = dict((Key, 0) for Key in AllPairs)

	for Word in ListOfWords:
		if len(Word) == 0:
			continue
		# First char
		Counts[(SPACE, Word[0])] += 1;
		# Last char
		Counts[(Word[len(Word)-1], SPACE)] += 1;
		# All chars between
		for i in range(0, len(Word)-1):
			Counts[(Word[i], Word[i+1])] += 1;
	
	return Counts

def buildMatrix(Counts):
	AllPairs = list(Counts.keys())
	UniqueChars = set([x[0] for x in AllPairs])
	SortedChars = sorted(UniqueChars)
	# Push new line sybom to the front
	SortedChars.insert(0, SortedChars.pop(SortedChars.index(SPACE)))
	
	Lines = []
	Lines.append(MATRIX_DELIMETER + MATRIX_DELIMETER.join(SortedChars))

	for FirstChar in SortedChars:
		Line = FirstChar
		for SecondChar in SortedChars:
			Line += MATRIX_DELIMETER + str(Counts[(FirstChar, SecondChar)])
		Lines.append(Line)
	return MATRIX_NEWLINE.join(Lines)
