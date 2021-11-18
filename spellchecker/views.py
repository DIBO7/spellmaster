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
			each_line = [] #to hold each word in a line as a string

			lines = text.decode().split("\n") #split on newlines

			for line in lines:
				file_per_line.append(line.replace("\r", ""))

			#NB: looping through text.decode() returns a string

		print(file_per_line)		
		
	return render(request, "mainpage.html", {})