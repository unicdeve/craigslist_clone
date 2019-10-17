from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base.html')


def search(request):
    new_search = request.POST.get('search')
    context = {
        'search': new_search
    }
    return render(request, 'app/search.html', context)

