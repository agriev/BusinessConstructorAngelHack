from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
# Create your views here.
from BCApp.models import BCBusinessUnit,BCBusinessModel,BCUser

@csrf_exempt
def home(request):
    context = { "name" : "name"}
    return render(request, "BCApp/index.html", context)

@csrf_exempt
def sign_in(request):
    context = { "name" : "name"}
    return render(request, "BCApp/signin.html", context)

@csrf_exempt
def model_list(request):
    models = BCBusinessModel.objects.all()
    context = { "models" : models}
    return render(request, "BCApp/models_list.html", context)

@csrf_exempt
def sign_up(request):
    context = { "name" : "name"}
    return render(request, "BCApp/signup.html", context)

@csrf_exempt
def recover_password(request):
    context = { "name" : "name"}
    return render(request, "BCApp/recover-password.html", context)

@csrf_exempt
def user_profile(request):
    context = { "name" : "name"}
    return render(request, "BCApp/user-profile.html", context)