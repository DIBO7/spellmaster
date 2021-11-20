from django.shortcuts import render
#from django.core.files import File
from django.core.files.storage import FileSystemStorage

# Create your views here.

def read_a_txt_file(file):
	list_of_lines = []
	with open(str(file), "r") as f:
		for lines in f:
			list_of_lines.append(f)
	'''
		fs = FileSystemStorage()
		filename = fs.save(document.name, document)
		#fs.url(filename) => the url to the file
		#print(read_a_txt_file(fs.url(filename)))

		file = fs.open(filename, "r")
		print("starts")
		for lines in file:
			print(lines)
		file = None #this is necessary to avoid File-In-Use-Error. this serves as a closing system (it closes the file)
		fs.delete(filename)
	'''

	return list_of_lines
	

from spellchecker import SpellChecker

spellcheckmaster = SpellChecker(distance=2, language="en")

def run_spellcheck(list_of_lines_list):
	result = []
	#list_of_lines_list is a list containing a sammler list of lines. The smaller list of lines contain words as strings
	line_counter = 1
	for lines in list_of_lines_list:
		#lines is a list of each word (strings) in one line
		result.append(one_line_spellcheck(lines, line_counter))
		line_counter += 1
	return result

def one_line_spellcheck(one_line, line_number=1):
	result = []
	wrong_words = spellcheckmaster.unknown(one_line)#find the wrong words..and we will correct them instead
	for words in wrong_words:
		result.append("{} in {} is wrong parhaps you mean {}".format(words, line_number, spellcheckmaster.correction(words)))
	return result


def MainPageViews(request):
	#request.GET.get("document-to-read")

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

			file_per_line = each_word_on_a_line #or file_per_line.append(...) instead!
			#remove '\r' and set whatever is left to "file_per_line"; thisw way I can work with file_per_line outside the for-loop


			#NB: looping through text.decode() returns a string
		corrected_file_per_line = run_spellcheck(file_per_line)
		print(file_per_line)
		print("---------CORRECTION 1-----------")
		print(corrected_file_per_line)
		
	return render(request, "mainpage.html", {})