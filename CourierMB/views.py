from django.views import generic
from django.shortcuts import get_object_or_404, render

def start_page(request):
    return render(request, 'start.html')