from lib import CharsOccur
from lib import AdjCounts
from lib import GroupDistance
from lib import Substrings

Text = [
	'To',
	'je',
	'moje',
	'testno',
	'besedilo',
	'razcepljeno',
	'na',
	'posamezne',
	'besede',
	'ki',
	'bojo',
	'sluzile',
	'kot',
	'testni',
	'vhod',
	'v',
	'moj',
	'program'
]

print(Substrings.sortRepeats(Substrings.getRepetedSubstrings(Text)))
