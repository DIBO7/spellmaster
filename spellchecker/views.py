from django.shortcuts import render

# Create your views here.


def MainPageViews(request):
	return render(request, "sample.html", {})