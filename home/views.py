from django.shortcuts import render, redirect
from .forms import Imageform
from .models import image
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import imageserializer
from django.contrib import messages
# Create your views here.


class images(APIView):
    def post(self,request):
        serializer=imageserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'done'})
        return Response(serializer.error)
    def get(self,request):
        data=image.objects.all()
        serializer=imageserializer(data,many=True)
        return Response(serializer.data)
def upload_image(request):
    if request.method == 'POST':
        form = Imageform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image uploaded successfully!')
            return redirect('upload-image')
        else:
            messages.error(request, 'Failed to upload image. Please try again.')
   
    form = Imageform()
    img=image.objects.all()
    
    return render(request, 'upload_image.html', {'form': form,'img':img})