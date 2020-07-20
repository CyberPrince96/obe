from django.shortcuts import render
from django.http import HttpResponse
from obe import settings
import os
# Create your views here.

def homepage(request):
	return render(request, 'showtopics/index.html')





def renderImg(request,imgname):
	uri = os.path.join(settings.BASE_DIR,"media/images/")
	image_data = open(uri+imgname, "rb").read()
	return HttpResponse(image_data, content_type="image/png")