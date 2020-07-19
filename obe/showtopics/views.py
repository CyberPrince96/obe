from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homepage(request):
	return render(request, 'showtopics/index.html')





def renderImg(request,imgname):
	image_data = open("/home/ubuntu/obe/obe/media/images/"+imgname, "rb").read()
	return HttpResponse(image_data, content_type="image/png")