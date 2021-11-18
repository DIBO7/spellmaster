from django.shortcuts import render
#from django.core.files import File
from django.core.files.storage import FileSystemStorage

# Create your views here.

def read_a_txt_file(file):
	list_of_lines = []
	with open(str(file), "r") as f:
		for lines in f:
			list_of_lines.append(f)
	return list_of_lines
	




def MainPageViews(request):
	#request.GET.get("document-to-read")

	if request.method=="POST" and request.FILES["document-to-read"]:
		document = request.FILES["document-to-read"]

		fs = FileSystemStorage()
		filename = fs.save(document.name, document)
		#fs.url(filename) => the url to the file
		#print(read_a_txt_file(fs.url(filename)))

		file = fs.open(filename, "r")
		print("starts")
		for lines in file:
			print(lines)


	return render(request, "mainpage.html", {})