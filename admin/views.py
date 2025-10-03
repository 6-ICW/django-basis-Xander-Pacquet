from django.shortcuts import render

# Create your views here.
def htmlResponse(request):
    return render(request, 'login.html')