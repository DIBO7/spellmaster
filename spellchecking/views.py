import time #using this to calculate the processing speed
from django.shortcuts import render
#from django.core.files import File
from django.core.files.storage import FileSystemStorage

from spellchecker import SpellChecker
# Create your views here.


spellcheckmaster = SpellChecker(distance=2, language="en")
spellcheckmaster.word_frequency.load_words(["s", "http", "https", "html", "css", "javascript", "100%"]) 
#.load_text("a string"), .load_text_file("./path_to_file.txt"), .load_dictionary("./path_to_file.json") OR .add("a single word"), .remove("a word from the dic")
#list of words that should NOT be flagged as incorrect. List will grow larger

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
	wrong_words = spellcheckmaster.unknown(one_line)#find the wrong words..and we will correct them
	for words in wrong_words:
		suggestion = spellcheckmaster.correction(words)

		if suggestion != words:
			result.append('"{}" in line {} is spelled incorrectly, parhaps you mean "{}"'.format(words, line_number, suggestion))
			#this is because the corrections are sometimes the same as the wrong words
		else:
			result.append('"{}" in line {} seems to be spelled incorrectly.'.format(words.upper(), line_number))
	return result


unwanted_characters = ["?", "!", '"', "(", ")", ",", ".", "/", "\r", "\t", ":", ";", "-", "_", "'"] 
#"." is problematic because file may contain .net or .com or .somethingelse..."'" is also problematic beacuse of "isn't"
#may use reges to fix that...BUT GOD, WE MUST AVOID REGEX for as long as we can...
#or parhaps "." and ":" may be replaced with spaces (" ") instead of ""

def strip_unwanted_txt_character(sentence):
	#removes unwanted characters that may be attched to the word and render it incorrect
	for char in unwanted_characters:
		if char in sentence:
			sentence = sentence.replace(char, " ")
			#replace with a space instaed, so "facebook.com" can be spell checked as "facebook" and "com" and NOT "facebookcom"
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
		process_start_time = time.time()
		document = request.FILES["document-to-read"]

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

		process_time_duration = time.time() - process_start_time

		if len(checked_file_per_line) < 1:
			check_remarks = "no spelling mistake spotted. Your file is error-free and the reading took {} seconds".format(round(process_time_duration, 4))
			status_class = "good-message"
		else:
			check_remarks = "{} spelling mistakes spotted in {} seconds!!".format(len(checked_file_per_line), round(process_time_duration, 4))
			#I did it like this instead of using .append() because I want this text to come first! so it has to be ontop

		
	return render(request, "mainpage.html", {"reports":checked_file_per_line, "doc":document, "remark": check_remarks, "css":status_class})