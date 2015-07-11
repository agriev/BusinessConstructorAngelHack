from django.shortcuts import render
from django.shortcuts import render_to_response
# Create your views here.

def home(request):
    context = { "name" : "name"}
    return render(request, "BCApp/home.html", context)