from django.shortcuts import render

# Create your views here.
def store(requests):
    context = None
    template = 'store.html'
    return render(requests, template, context)