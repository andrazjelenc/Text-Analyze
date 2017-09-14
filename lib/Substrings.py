
def getRepetedSubstrings(ListOfWords):
	AllSubstrings = []
	# Fill list with all substrings lenght more than one
	for Word in ListOfWords:
		AllSubstrings.extend([Word[i:j+1] for i in range(len(Word)) for j in range(i+1,len(Word))])
	
	Repeats = {}
	# Count repeted substrings
	for Substring in AllSubstrings:
		if Substring not in Repeats:
			Cnt = AllSubstrings.count(Substring)
			if Cnt > 1:
				Repeats[Substring] = Cnt
	# Remove substrings of larger substring
	Substrings = list(Repeats.keys())
	for Sstr in Substrings:
		for Sstr2 in Repeats.keys():
			if Sstr != Sstr2 and Sstr in Sstr2 and Repeats[Sstr] == Repeats[Sstr2]:
				del Repeats[Sstr]
				break
	
	return Repeats
	
def sortRepeats(Repeats):
	List = [(k, v) for k, v in Repeats.items()]
	return sorted(List, key=lambda x: (len(x[0]), x[1]), reverse=True)
