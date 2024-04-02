from django.shortcuts import render


# Create your views here.
def indicators(request):
    return render(request, "indicators.html")
