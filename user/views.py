from django.shortcuts import render

# Create your views here.
def user_man(request):
    return render (request, 'user.html')