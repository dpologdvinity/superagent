import re
def text_match_wordz_middle(text):
	return re.search(r'\Bz\B',  text) is not None
