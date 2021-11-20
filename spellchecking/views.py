from django.shortcuts import render
#from django.core.files import File
from django.core.files.storage import FileSystemStorage

from spellchecker import SpellChecker
# Create your views here.


spellcheckmaster = SpellChecker(distance=2, language="en")

def run_spellcheck(list_of_lines_list):
	result = []
	#list_of_lines_list is a list containing a sammler list of lines. The smaller list of lines contain words as strings
	line_counter = 1
	for lines in list_of_lines_list:
		#lines is a list of each word (strings) in one line
		result += one_line_spellcheck(lines, line_counter)
		line_counter += 1
	return result

def one_line_spellcheck(one_line, line_number=1):
	result = []
	wrong_words = spellcheckmaster.unknown(one_line)#find the wrong words..and we will correct them instead
	for words in wrong_words:
		suggestion = spellcheckmaster.correction(words)

		if suggestion != words:
			result.append('"{}" in line {} is spelled incorrectly, parhaps you mean "{}"'.format(words, line_number, suggestion))
			#this is because the corrections are sometimes the same as the wrong words
		else:
			result.append('"{}" in line {} is spelled incorrectly.'.format(words.upper(), line_number))
	return result


def MainPageViews(request):
	#request.GET.get("document-to-read")

	checked_file_per_line = []
	document = False

	if request.method=="POST" and request.FILES["document-to-read"]:
		document = request.FILES["document-to-read"]

		chunk_of_file = document.chunks() #.chunks() breakdown large files onto chunks and read them; to avoid overwhelming the memory.
		#PS: .chunks() return b strings (b'___')
		
		file_per_line = [] #I want to be able to tell user that the 3rd word on XXX line is wrong...hence keeping track of the lines
		#holds a line of words as a list
		for text in chunk_of_file:
			#chunk_of_file here is the entire document (or a fraction of it) in a "b string"

			lines = text.decode().split("\n") #split on newlines
			#lines is a list ot the chunked_document, line by line (with '\r' probably in them)

			each_word_on_a_line = []

			#to remove the '\r' then;
			for line in lines: #line represent one line in the document
				each_word_on_a_line.append(line.replace("\r", "").split())
				#each_word_on_a_line -> a list of every word (as a string) in a particular line within the document
				'''
				There is a problem with '.splt()' here. The words are seperated at 'spaces only'. This must expand to separete at coma, brackets, fullstop, exclamation
				or atleast those things should be stripped out too.
				'''

			file_per_line = each_word_on_a_line #or file_per_line.append(...) instead!
			#remove '\r' and set whatever is left to "file_per_line"; thisw way I can work with file_per_line outside the for-loop


			#NB: looping through text.decode() returns a string
		checked_file_per_line = run_spellcheck(file_per_line)
		#just incase no spelling mistake is found!
		if len(checked_file_per_line) < 1:
			checked_file_per_line = ["no spelling mistake spotted!!"]
		else:
			checked_file_per_line.append("{} spelling mistakes spotted!!".format(len(checked_file_per_line)))

		
	return render(request, "mainpage.html", {"reports":checked_file_per_line, "name":document})