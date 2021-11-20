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


unwanted_characters = ["?", "!", '"', "(", ")", ",", ".", "/", "\r", "\t", ":", ";"] #"." is problematic because file may contain .net or .com or .somethingelse...
#may use reges to fix that...BUT GOD, WE MUST AVOID REGEX for as long as we can...

def strip_unwanted_txt_character(sentence):
	#removes unwanted characters that may be attched to the word and render it incorrect
	for char in unwanted_characters:
		if char in sentence:
			sentence = sentence.replace(char, "")
		else:
			pass

	return sentence


def MainPageViews(request):
	#request.GET.get("document-to-read")

	checked_file_per_line = []
	document = False
	status_class = "error-message" #for css purposes, could be "error-message" or "good-message" (at the time of writing)
	check_remarks = ""

	if request.method=="POST" and request.FILES["document-to-read"]:
		document = request.FILES["document-to-read"]

		chunk_of_file = document.chunks() #.chunks() breakdown large files onto chunks and read them; to avoid overwhelming the memory.
		#PS: .chunks() return b strings (b'___')
		
		file_per_line = [] #I want to be able to tell user that 'XX word on XX line is wrong'...hence keeping track of the lines
		#holds a line of words as a list
		for text in chunk_of_file:
			#chunk_of_file here is the entire document (or a fraction of it) in a "b string"

			lines = text.decode().split("\n") #split on newlines #we do 
			#lines is a list ot the chunked_document, line by line (with '\r' probably in them)

			each_word_on_a_line = []

			#to remove the '\r' then;
			for line in lines: #line represent one line in the document
				each_word_on_a_line.append(strip_unwanted_txt_character(line).split())
				#each_word_on_a_line -> a list of every word (as a string) in a particular line within the document				

			file_per_line = each_word_on_a_line #or file_per_line.append(...) instead!
			#remove '\r' and set whatever is left to "file_per_line"; thisw way I can work with file_per_line outside the for-loop


			#NB: looping through text.decode() returns a string
		checked_file_per_line = run_spellcheck(file_per_line)
		#just incase no spelling mistake is found!
		if len(checked_file_per_line) < 1:
			check_remarks = ["no spelling mistake spotted!! Congrats, Your file is clean!!"]
			status_class = "good-message"
		else:
			check_remarks = "{} spelling mistakes spotted!!".format(len(checked_file_per_line))
			#I did it like this instead of using .append() because I want this text to come first! so it has to be ontop

		
	return render(request, "mainpage.html", {"reports":checked_file_per_line, "doc":document, "remark": check_remarks, "css":status_class})