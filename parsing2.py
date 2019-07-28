import re

global file_list, func_def_in_file_dict
file_list = []
func_def_in_file_dict = {}


class Node:
	def __init__(self,name):
		self.name = name
		self.children = []

	def add_child(self,obj):
		self.children.append(obj)

class hierarchyTree:

	def getFileLine(self,file_name):
		with open(file_name) as file:	
			file_lines = file.read().strip()
		return file_lines

	def hashTagParser(self,current_file):
		# ['main.cpp', 'HelloWorldHelper.hpp', 'StandardHelper.hpp']
		file_list.append(current_file)
		file_lines = self.getFileLine(current_file)
		hash_file_list = re.findall("\#[a-zA-Z]+\s\"\w+\.\w+\"",file_lines)
			
		for file_name in hash_file_list:
			next_file = re.findall('\"(.+?)\"',file_name)
			next_file = ''.join(next_file)
			if next_file:
				self.hashTagParser(next_file)
		return file_list	 


	def functionDefinitionParser(self,file_name): 
		# {int main() : main.cpp}
		file_lines = self.getFileLine(file_name)
		
		func_def_in_file = re.findall("\w+\s\w+\(\w*[a-zA-Z\:\w*\s\)]*\s*\{",file_lines)
		for func_def in func_def_in_file:
			func_def = func_def.replace('{','')
			func_def_in_file_dict[func_def] = file_name
		return func_def_in_file_dict
		

	def functionCalledInFileParser(self,file_name):
		# main.cpp called-->  ['main()', 'test_message()', 'get_code()', 'myPrint("ERROR")']
		file_lines = self.getFileLine(file_name)
		func_called_in_file = re.findall("\w+\([\"\w+\",]*[\w+,]*[\w+]*\)",file_lines)
		return func_called_in_file
		
	# def funcInFunc(self,function_name_list,func_def_in_file_d):

	
	def constructNode(self,name,children_list):
		root = Node(name)
		for child in children_list:
			root.add_child(child)
		print 'root name:', root.name
		print root.children

	def construcTree(self):
		file_list = self.hashTagParser("main.cpp")
		for file_name in file_list:
			func_called_in_file = self.functionCalledInFileParser(file_name)
			self.constructNode(file_name,func_called_in_file)
			func_def_in_file_d = self.functionDefinitionParser(file_name) # int main()  : main.cpp

		# for key in func_def_in_file_d:
		# 	print key,':',func_def_in_file_d[key]



if __name__ == '__main__':
	tree = hierarchyTree()
	tree.construcTree()


