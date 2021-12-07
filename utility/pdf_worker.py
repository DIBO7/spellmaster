#import base64
#print(base64.a85decode(chunk).decode('utf-8')) #chuck is the chunk of file to be read!
import PyPDF2
from scope.pdf_tools import convert_pdf_to_string
from scope.word_editor import strip_unwanted_txt_character
from scope.spelling_tools import run_spellcheck




def Read_Pdf_File(document):

	#reader = PyPDF2.PdfFileReader(document)
	#reader_on_page = 0
	#while reader_on_page < reader.numPages:
	pdf_stringed_text = strip_unwanted_txt_character(convert_pdf_to_string(document))
	#pdf_stringed_text.split("\n") #this is a list with lines_of_sentences in it
	line_list_of_wordlist = []

	for every_line in pdf_stringed_text.split("\n"):
		words_on_each_line = every_line.split() #a list of words on every_line
		line_list_of_wordlist.append(words_on_each_line)

	analysis = run_spellcheck(line_list_of_wordlist)


	return analysis

'''
pdf_reader = PyPDF2.PdfFileReader(doc)
		reader_on_page = 0 #to start the reader from page 1
		while reader_on_page < pdf_reader.numPages:
			print("--------------------------------------")
			print(pdf_reader.getPage(reader_on_page).extractText())
			reader_on_page += 1
'''