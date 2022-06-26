from django.shortcuts import render

# Create your views here.
def loremindex(request):
    return render(request, 'paginalorem/loremindex.html')