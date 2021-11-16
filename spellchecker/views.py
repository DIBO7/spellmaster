from django.shortcuts import render

# Create your views here.
'''
def open_a_txt_file(file):
	with open(file, "r"):
		print 
	#opens a file
'''



def MainPageViews(request):


	return render(request, "mainpage.html", {})