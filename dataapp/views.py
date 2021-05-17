from django.shortcuts import render
from django.http import HttpResponse
from dataapp.models import entry
# Create your views here.
def home(request):
    if request.POST:
        name = request.POST['name']
        entry(name=name).save()
    return render(request,'home.html')

def send(request):

        return HttpResponse("<h1>data is submitted</h1>")

def show(request):
    data = entry.objects.all()
    return render(request,'show.html',{'data':data})
def delete(request):
    id = request.POST['id']
    entry.objects.filter(id=id).delete()
    return HttpResponseRedirect("show")