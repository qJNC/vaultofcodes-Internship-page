from django.shortcuts import render

# Create your views here.
def internship(request):
    return render (request, 'internship_page.html')