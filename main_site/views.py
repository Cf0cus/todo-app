from django.shortcuts import render



def home(request):
    # print("f")
    return render(request,"main_site/home.html")