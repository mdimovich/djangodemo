from django.shortcuts import render

contact_string = "If you would like to contact me, please e-mail me at mdimovich@gmail.com"
contact_string2 = "If you would like to check out some of my personal projects, please visit my GitHub page at github.com/mdimovich"

def index(request):
    return render(request, 'personal/home.html')


def contact(request):
    return render(request, 'personal/basic.html', {'contact': [contact_string, contact_string2]})

def blog(request):
    return render(request, 'personal/blog.html')