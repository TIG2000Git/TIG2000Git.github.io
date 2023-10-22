from django.shortcuts import render

# Create your views here.
def start(requst):
    return render(requst, 'start.html')