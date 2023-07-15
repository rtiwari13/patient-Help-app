from django.http import HttpResponseRedirect
from django.shortcuts import render 
from .forms import *
from rest_framework import generics
from .serializers import *
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def home(request):

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            context = {'msg' : '<span style="color: green;">  </span>'}
            return render(request, "home.html", context)
    else:
        form = UploadFileForm()
    return render(request, 'home.html', {'form': form})


def handle_uploaded_file(f):
    with open(f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            
class PatientDetails(generics.ListAPIView):
    queryset = Details.objects.all()
    serializer_class = DetailSerializer 



