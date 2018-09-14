from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect 

# Create your views here.
def index(request):
    return render(request, "graphapp/index.html")
