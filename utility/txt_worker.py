from scope.spelling_tools import run_spellcheck
from scope.word_editor import strip_unwanted_txt_character

'''
This file is responsible for reading .txt files.
It returns 
'''


def Read_Txt_File(document):#document = request.FILES["document-to-read"]
	chunk_of_file = document.chunks() #.chunks() breakdown large files onto chunks and read them; to avoid overwhelming the memory.
	#PS: .chunks() return b strings (b'___')
	
	file_per_line = [] #I want to be able to tell user that 'XX word on XX line is wrong'...hence keeping track of the lines
	#holds a line of words as a list
	for text in chunk_of_file:
		#chunk_of_file here is the entire document (or a fraction of it) in a "b string"

		lines = strip_unwanted_txt_character(text.decode()).split("\n")
		#text.decode().split("\n") #split on newlines #we do 
		#lines is a list ot the chunked_document, line by line (with '\r' probably in them)
		#remove the unwanted characters first and strip on newlines #this seems to be faster but by very little amount that it is almost not noticeable

		each_word_on_a_line = []

		#to remove the '\r' then;
		for line in lines: #line represent one line in the document
			each_word_on_a_line.append(line.split())
			#each_word_on_a_line -> a list of every word (as a string) in a particular line within the document				

		file_per_line = each_word_on_a_line #or file_per_line.append(...) instead!
		#remove '\r' and set whatever is left to "file_per_line"; thisw way I can work with file_per_line outside the for-loop


		#NB: looping through text.decode() returns a string
	checked_file_per_line = run_spellcheck(file_per_line)
	#just incase no spelling mistake is found!

	return checked_file_per_line