import re

global tup_list
tup_list = []

def beginToParse(start_file):
	next_file = hashTagParser(start_file) # detect '# include ...'

	function_file_tup = functionDefinitionParser(start_file,next_file)
	tup_list.append(function_file_tup)	

def getFileLine(file_name):
	with open(file_name) as file:	
		file_lines = file.read().strip()
	return file_lines

def hashTagParser(current_file):
	file_lines = getFileLine(current_file)
	hash_file_list = re.findall("\#[a-zA-Z]+\s\"\w+\.\w+\"",file_lines)
		
	for file_name in hash_file_list:
		next_file = re.findall('\"(.+?)\"',file_name)
		next_file = ''.join(next_file)
		if next_file:
			beginToParse(next_file)
		return next_file

def functionDefinitionParser(current_file, next_file): 
	file_lines = getFileLine(current_file)
	function_called_d = functionInFileParser(current_file,file_lines)

	function_def_in_file = re.findall("\w+\s\w+\([\"\w+\",]*[\w+,]*[\w+]*\)",file_lines)
	function_def_tuple = tuple((current_file,function_called_d))
	return function_def_tuple
		
def functionInFileParser(file_name,file_lines):
	function_called_d = {}
	function_called_in_file = re.findall("\w+\([\"\w+\",]*[\w+,]*[\w+]*\)",file_lines)
	value_assign = re.findall("\w+\s\w+\s*\=\s*[a-zA-Z0-9]+\;",file_lines)
	if value_assign is not None:
		function_called_in_file.append(value_assign)

	func_key = str(function_called_in_file[0])
	function_called_d[func_key] = function_called_in_file
	# function_called_d[file_name] = function_called_in_file 	
	
	return function_called_d

if __name__ == '__main__':
	beginToParse("main.cpp")
	tup_list.reverse()
	for tup in tup_list:
		print tup[1], '---/', tup[0],'\n'


