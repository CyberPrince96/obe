from django.shortcuts import render

# Create your views here.

def homepage(request):
	return render(request, 'showtopics/index.html')





def renderImg(request,imgname):
	image_data = open("images/"+imgname, "rb").read()
	return HttpResponse(image_data, content_type="image/png")