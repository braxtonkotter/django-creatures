from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'creaturesApp/index.html', {'title':'Home'})
def about(request):
    return render(request, 'creaturesApp/about.html', {'title':'About'})
def account(request):
    return render(request, 'creaturesApp/account.html', {'title':'Account'})
def adminDashboard(request):
    return render(request, 'creaturesApp/admin-dashboard.html', {'title':'Admin Dashboard'})
def details(request):
    return render(request, 'creaturesApp/details.html', {'title':'Details'})
def results(request):
    return render(request, 'creaturesApp/results.html', {'title':'Search Results'})
def signIn(request):
    return render(request, 'creaturesApp/sign-in.html', {'title':'Sign In'})
def signUp(request):
    return render(request, 'creaturesApp/sign-up.html', {'title':'Sign Up'})
def tickets(request):
    return render(request, 'creaturesApp/tickets.html', {'title':'Tickets'})
