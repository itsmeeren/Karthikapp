from django.shortcuts import render,HttpResponse,redirect
# from datetime import datetime
from .models import Contact
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.http import HttpResponse, FileResponse
from django.conf import settings
import os
from .forms import ImageModelForm

# Create your views here.

def index(request):
    # return HttpResponse("/static/videos/ghost.mp4")
    return render(request,"index.html")
def spoofing(request):
    return render(request,"arp.html")
def ip(request):
    return render(request,"upload_to.html")
def mac(request):
    return render(request,"mac.html")
def randommac(request):
    return render(request,"search.html")


def success_page(request):
    return render(request, 'success_page_template.html')



def help(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()



    return render(request, "help.html")








def search(request):
    if request.method == "POST":
        search_query = request.POST.get("search_query", "")
        if search_query:
            return render_video(request, search_query)
    return HttpResponse("Video not found")

def render_video(request, search_query):

    video_path = "/home/karthik/django/hello/media/videos"
    video_file_path = os.path.join(video_path, f'{search_query}.mp4')

    try:

        if os.path.exists(video_file_path):

            response = FileResponse(open(video_file_path, 'rb'), content_type='video/mp4')
            return response
        else:

            return HttpResponse("Video not found", status=404)
    except Exception as e:

        return HttpResponse(f"An error occurred: {str(e)}", status=500)




# views.py


def search_image(request):
    if request.method == "POST":
        search_image_name = request.POST.get("search_image", "")
        if search_image_name:
            return render_image(request, search_image_name)
    return HttpResponse("Image not found")
# writing the same function for the rendering of the images


# i can have as many of images in karthik/project/images folder i can render based on the client request




def render_image(request, search_image_name):
    image_path = "/home/karthik/django/hello/media/images"
    image_file_path = os.path.join(image_path, f'{search_image_name}.jpg')

    try:
        if os.path.exists(image_file_path):
            with open(image_file_path, 'rb') as image_file:
                # for reading the file from karthiks directory i can create my directory for that also
                image_data = image_file.read()
# this is to tak  the infon
                response = HttpResponse(image_data, content_type='image/jpeg')
                return response
        else:
            # i did not understand this this is somemthing string related to python with html
            return HttpResponse("Image not found", status=404)
    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}", status=500)

# views.py


# views.py






def image_upload_view(request):
    if request.method == 'POST':
        form = ImageModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_page')  #redirect changes tu url endpoint to my success which i defined in my views
    else:
        form = ImageModelForm()

    return render(request, 'upload_to.html', {'form': form})


#next task to be completed is

    #1 write view for the info about yourself
    #2 write html to render videos and images in the videos and images instance
