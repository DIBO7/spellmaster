import time #using this to calculate the processing speed
from django.shortcuts import render
from django.http import HttpResponse
#from django.core.files import File
from django.core.files.storage import FileSystemStorage

from utility.txt_worker import Read_Txt_File
from utility.pdf_worker import Read_Pdf_File
# Create your views here.

'''
IN DJANGO DOCS, I FOUND ".__iter__()" which reads line by line..look into this, might be good for performance
'''

accepted_file_formats = [
	"text/plain", #also .charset returns None
	"application/pdf", #charset for pdf returns None,
]


def MainPageViews(request):
	#request.GET.get("document-to-read")	
	checked_file_per_line = []
	document = False
	status_class = "error-message" #for css purposes, could be "error-message" or "good-message" (at the time of writing)
	check_remarks = ""

	if request.method=="POST" and request.FILES["document-to-read"]:
		process_start_time = time.time()
		document = request.FILES["document-to-read"]
		#use either document.content_type or document.charset to determine how to read it but so far .charset has been returning "None" for all files
		if document.content_type == "text/plain":
			checked_file_per_line = Read_Txt_File(document)
		elif document.content_type == "application/pdf":
			checked_file_per_line = Read_Pdf_File(document)
		else:
			#this would be hard to comeby as the fronend also checks file formats before permiting user to proceed
			return HttpResponse(status=400)

		process_time_duration = time.time() - process_start_time

		#error is checked by looking at the 'checked_file_per_line' which containes corrected words...if it is not empty, there were errors spotted!
		if len(checked_file_per_line) < 1:
			check_remarks = "no spelling mistake spotted. Your file is error-free and the reading took {} seconds".format(round(process_time_duration, 4))
			status_class = "good-message"
		else:
			check_remarks = "{} spelling mistakes spotted in {} seconds!!".format(len(checked_file_per_line), round(process_time_duration, 4))
			#I did it like this instead of using .append() because I want this text to come first! so it has to be ontop

		
	return render(request, "mainpage.html", {"reports":checked_file_per_line, "doc":document, "remark": check_remarks, "css":status_class})