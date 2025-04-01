from django.shortcuts import render

def gabe_view(request):
    return render(request,"template1/index.html")