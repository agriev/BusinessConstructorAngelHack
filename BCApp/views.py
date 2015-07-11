from django.shortcuts import render
from django.shortcuts import render_to_response
# Create your views here.
from BCApp.models import BCBusinessUnit,BCBusinessModel,BCUser

def home(request):
    context = { "name" : "name"}
    return render(request, "BCApp/home.html", context)

def model_list(request):
    models = BCBusinessModel.objects.all()
    context = { "models" : models}
    return render(request, "BCApp/models_list.html", context)