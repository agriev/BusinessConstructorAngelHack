from django.shortcuts import render
from django.shortcuts import render_to_response
# Create your views here.

def home(request):

    render_to_response(request, "BCApp/home.html", {})