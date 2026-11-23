import re 
def check_str(string): 
	regex = '^[aeiouAEIOU][A-Za-z0-9_]*'
	return re.search(regex, string)
