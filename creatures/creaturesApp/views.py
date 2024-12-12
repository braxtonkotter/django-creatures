from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from .models import *

# Create your views here.
def index(request):
    creatures = creature.objects.all().order_by('name')
    print(request.user.is_superuser)
    return render(request, 'creaturesApp/index.html', {'title':'Home', 'creatures':creatures})
def about(request):
    return render(request, 'creaturesApp/about.html', {'title':'About'})
def account(request):
    tickets = ticket.objects.all().filter(user__icontains=request.user.email)
    return render(request, 'creaturesApp/account.html', {'title':'Account', 'tickets':tickets})
def adminDashboard(request):
    open_tickets = ticket.objects.all().filter(status__icontains='open')
    closed_tickets = ticket.objects.all().filter(status__icontains='accepted')
    closed_tickets |= ticket.objects.all().filter(status__icontains='rejected')
    return render(request, 'creaturesApp/admin-dashboard.html', {'title':'Admin Dashboard', 'open_tickets':open_tickets, 'closed_tickets':closed_tickets})
def details(request, item_id):
    creatures = creature.objects.get(pk=item_id)
    return render(request, 'creaturesApp/details.html', {'title':'Details', 'creatures':creatures})

def results(request):
    return render(request, 'creaturesApp/results.html', {'title':'Search Results'})

def results(request, id):
    match id:
        case 0: return render(request, 'creaturesApp/results.html', {'title':'Search Results For Africa Region', 'results':creature.objects.all().filter(region__icontains='Africa')})
        case 1: return render(request, 'creaturesApp/results.html', {'title': 'Search Results For South America Region', 'results': creature.objects.all().filter(region__icontains='South America')})
        case 2: return render(request, 'creaturesApp/results.html', {'title': 'Search Results For North America Region', 'results': creature.objects.all().filter(region__icontains='North America')})
        case 3: return render(request, 'creaturesApp/results.html', {'title': 'Search Results For Middle East Region', 'results': creature.objects.all().filter(region__icontains='Middle East')})
        case 4: return render(request, 'creaturesApp/results.html', {'title': 'Search Results For Europe Region', 'results': creature.objects.all().filter(region__icontains='Europe')})
        case 5: return render(request, 'creaturesApp/results.html', {'title': 'Search Results For Asia Pacific Region', 'results': creature.objects.all().filter(region__icontains='Asia Pacific')})
def signUp(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
            login(request, user)
            return redirect('index')

    return render(request, 'creaturesApp/sign-up.html', {'title':'Sign Up'})
def create(request):
    if request.method == 'POST':
        created_ticket = ticket.objects.create(name=request.POST['name'], description=request.POST['description'], mythology=request.POST['myth'], region=request.POST['region'], ref_link=request.POST['ref_link'], status='open', user=request.user.email)
        created_ticket.save()
        return redirect('account')
    return render(request, 'creaturesApp/tickets.html', {'title':'Create Ticket'})
def tickets(request, item_id):
    if request.method == 'POST':
        edit_ticket = ticket.objects.get(pk=item_id)

        edit_ticket.name = request.POST['name']
        edit_ticket.description = request.POST['description']
        edit_ticket.myth = request.POST['myth']
        edit_ticket.region = request.POST['region']
        edit_ticket.ref_link = request.POST['ref_link']
        edit_ticket.status = 'open'
        edit_ticket.save()
        return redirect('account')

    ticket_selected = ticket.objects.get(pk=item_id)
    return render(request, 'creaturesApp/tickets.html', {'title':'Edit Ticket', 'ticket': ticket_selected})

def delete(request, item_id):
    ticket_to_delete = ticket.objects.get(pk=item_id)
    ticket_to_delete.delete()
    return redirect('account')


def search(request):
    if request.method == 'POST':
        if(request.POST['name'] != ''):
            creatures = creature.objects.all().filter(name__icontains=request.POST['name'])
        elif (request.POST['mythology'] != ''):
            creatures = creature.objects.all().filter(mythology__icontains=request.POST['mythology'])
        else:
            creatures = creature.objects.none()
            if request.POST.get('africa_check') == 'on':
                creatures |= creature.objects.all().filter(region__icontains='Africa')
            if request.POST.get('asia_check') == 'on':
                creatures |= creature.objects.all().filter(region__icontains='Asia')
            if request.POST.get('europe_check') == 'on':
                creatures |= creature.objects.all().filter(region__icontains='Europe')
            if request.POST.get('middle_east_check') == 'on':
                creatures |= creature.objects.all().filter(region__icontains='Middle East')
            if request.POST.get('north_america_check') == 'on':
                creatures |= creature.objects.all().filter(region__icontains='North America')
            if request.POST.get('south_america_check') == 'on':
                creatures |= creature.objects.all().filter(region__icontains='South America')
        return render(request, 'creaturesApp/results.html', {'title':'Search Results', 'results':creatures})
    return render(request, 'creaturesApp/search.html', {'title':'Search'})
def popular(request):
    array = ['Zombie', 'Sphinx', 'Yeti', 'Gnome', 'Kraken', 'Troll', 'Golem', 'Ghoul', 'Mermaid', 'Sirens']
    print("Here")
    creatures = creature.objects.none()
    for items in array:
        creatures |= creature.objects.all().filter(name__icontains=items)
    return render(request, 'creaturesApp/results.html', {'title':'Popular Results', 'results':creatures})

def message(request, ticket_id, ruling_id):
    message_ticket = ticket.objects.get(pk=ticket_id)

    if request.method == 'POST':
        message_ticket.message = request.POST['message']
        if ruling_id == 0:
            message_ticket.status = 'accepted'
            create_creature = creature.objects.create(name=message_ticket.name, description=message_ticket.description, mythology=message_ticket.mythology, region=message_ticket.region, ref_link=message_ticket.ref_link)
            create_creature.save()
        else:
            message_ticket.status = 'rejected'
        message_ticket.save()
        return redirect('admin-dashboard')

    return render(request, 'creaturesApp/message.html', {'title':'Message', 'ticket':message_ticket})
