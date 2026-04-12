from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def dashboard(request):
    return render(request, 'dashboard.html')
def sales(request):
    return render(request, 'sales.html')
def stock(request):
    return render(request, 'stock.html')
def creditsales(request):
    return render(request, 'creditsales.html')
def deposits(request):
    return render(request, 'deposits.html')
def transport(request):
    return render(request, 'transport.html')
def reports(request):
    return render(request, 'reports.html')




