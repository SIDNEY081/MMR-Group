from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    context = {
        'page_title': 'About MMR Group',
        'mission': 'To empower progress through digital and construction excellence.'
    }
    return render(request, 'about.html', context)

def ventures(request):
    return render(request, 'ventures/ventures.html')

def tech_solutions(request):
    return render(request, 'ventures/tech.html')

def construction(request):
    return render(request, 'ventures/construction.html')

def aluminium_glass(request):
    return render(request, 'ventures/aluminium.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def contact(request):
    return render(request, 'contact.html')