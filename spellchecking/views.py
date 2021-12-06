import time #using this to calculate the processing speed
from django.shortcuts import render
#from django.core.files import File
from django.core.files.storage import FileSystemStorage

from utility.txt_worker import Read_Txt_File
# Create your views here.



def MainPageViews(request):
	#request.GET.get("document-to-read")	
	checked_file_per_line = []
	document = False
	status_class = "error-message" #for css purposes, could be "error-message" or "good-message" (at the time of writing)
	check_remarks = ""

	if request.method=="POST" and request.FILES["document-to-read"]:
		process_start_time = time.time()
		document = request.FILES["document-to-read"]
		checked_file_per_line = Read_Txt_File(request.FILES["document-to-read"])

		process_time_duration = time.time() - process_start_time

		if len(checked_file_per_line) < 1:
			check_remarks = "no spelling mistake spotted. Your file is error-free and the reading took {} seconds".format(round(process_time_duration, 4))
			status_class = "good-message"
		else:
			check_remarks = "{} spelling mistakes spotted in {} seconds!!".format(len(checked_file_per_line), round(process_time_duration, 4))
			#I did it like this instead of using .append() because I want this text to come first! so it has to be ontop

		
	return render(request, "mainpage.html", {"reports":checked_file_per_line, "doc":document, "remark": check_remarks, "css":status_class})