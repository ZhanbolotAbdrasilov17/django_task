from django.shortcuts import render

# Create your views here.
def post_list(request):
    n = 'Abi'
    return render(request, 'blog/index.html', context = {'name':n})

def home(request):
    return render(request, 'blog/index.html')
def about(request):
    return render(request, 'blog/about.html')
def contacts(request):
    return render(request, 'blog/contacts.html')
def galary(request):
    return render(request, 'blog/galary.html')