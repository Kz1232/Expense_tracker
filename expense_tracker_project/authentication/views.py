from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def testview(request):
    # return HttpResponse("This is inside the authenticate apps")
    return render(request ,"authentication/login.html")