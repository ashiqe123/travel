from django.shortcuts import render
from travelapp.models import Travel,recent

# Create your views here.
def home(request):
    key=Travel.objects.all()
    obj=recent.objects.all()

    return render(request,'index.html',{'key':key,'obj':obj})