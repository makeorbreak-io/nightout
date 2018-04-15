from django.core import serializers
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import DetailView

from  .forms import EventForm, NightForm
from .models import Events, User, Night, Dividendos, Expenses
from social_django.models import UserSocialAuth

from django.contrib.auth.decorators import login_required
from django.utils import timezone

import random
import itertools
import requests

def postlogin(request):
    updateProfilePicture(request.user)
    addFriendships(request.user)
    return redirect(index)

def index(request):
    title = 'nightout'
    sitename = 'Hello World'
    user = request.user


    if not user.is_authenticated:
        return redirect('login')

    context = {'title' : title, 'sitename' : sitename, 'user':user ,'items' : feedEvents(user)}

    return render(
        request,
        'mainsite.html',
        context
    )
    #return HttpResponse("Hello, world.")

def createEvent(request):
    title = 'nightout'

    context = {'title' : title, }

    if request.method == 'POST':
        form = EventForm(request.POST)
        print(form.errors)

        if form.is_valid():
            event_data = Events()
            event_data.title = form.cleaned_data['title']
            event_data.description = form.cleaned_data['description']
            # event_data.image = form.cleaned_data['image']
            event_data.time = form.cleaned_data['time']
            event_data.date = form.cleaned_data['date']
            event_data.local = form.cleaned_data['local']
            event_data.private = form.cleaned_data['private']
            event_data.price = form.cleaned_data['price']

            event_data.creator = User.objects.get(pk=request.user.id)

            event_data.save()
            # event_data.pk = '0'

            return HttpResponseRedirect('events/' + str(event_data.pk))
        else:
            context['error'] = 'Not valid'
            return render(request, 'mainsite.html', context)
    else:
        form = EventForm()
        context['form'] = form

        return render(request, 'createEvent.html', context)

def planNight(request):
    title = 'nightout'

    context = {'title' : title}

    if request.method == 'POST':
        form = NightForm(request.POST)

        if form.is_valid():
            ev = repeated_events(form.cleaned_data['events'])

            if ev is None or len(ev.keys()) > 1:

                context['repeated_event'] = ev
                context['form'] = NightForm(initial={'title' : form.cleaned_data['title']})
                return render(request, 'planNight.html', context)

            else:
                night_data = Night()
                try:
                    night_data = Night.objects.get(title=form.cleaned_data['title'])
                except Exception:
                    night_data.title = form.cleaned_data['title']
                    night_data.save()

                # night_data = Night.objects.get(title=form.cleaned_data['title'])

                night_data.events.add(Events.objects.get(pk=list(ev.keys())[0]))
                night_data.user.add(User.objects.get(first_name=form.cleaned_data['user']))

                parse = Night.objects.filter(title=form.cleaned_data['title'])
                cur_users = User.objects.filter(first_name=form.cleaned_data['user'])

                # context['users'] = get_users()
                context['subbed_events'] = get_subscribed_events(parse)
                context['form'] = NightForm(initial={'title' : form.cleaned_data['title']})
                
                return render(request, 'planNight.html', context)
        else:
            context['error'] = 'Not valid'
            return render(request, 'mainsite.html', context)
    else:
        form = NightForm()

        context['form'] = form

        return render(request, 'planNight.html', context)

def search(request):
    redirect(index)

def myNights(request):
    user = request.user
    context = {'items': user.attending.all()}
    return render(request, 'my_night.html', context)

def myEvents(request):
    user = request.user
    context = {'events': user.events.all()}
    return render(request, 'my_events.html', context)

class NightsDetailView(DetailView):
    template_name='night_detail.html'
    model = Night

    def get_context_data(self, **kwargs):
        context = super(NightsDetailView, self).get_context_data(**kwargs)
        user = self.request.user
        nightID = self.kwargs['pk']
        night = Night.objects.get(pk=nightID)
        context['events'] = night.events.all()
        context['friends'] = night.user.all()
        context['expenses'] = night.expenses.all()
        print(context)
        return context

class EventsDetailView(DetailView):
    template_name='events_detail.html'
    model = Events

    def get_context_data(self, **kwargs):
        context = super(EventsDetailView, self).get_context_data(**kwargs)
        eventID = self.kwargs['pk']
        event = Events.objects.get(pk=eventID)
        user = self.request.user
        context['friends'] = getFriends(user,event)
        return context

class UserDetailView(DetailView):
    template_name='user_detail.html'
    model = User

def getFriends(user,event):
    userQ = User.objects.get(pk=user.id)
    goingTo = event.users.values_list('id',flat=True)
    f = userQ.friends.filter(id__in = goingTo)
    return f

def feedEvents(user):
    now = timezone.now()

    userQ = User.objects.get(pk=user.id)
    attending = userQ.events.all().order_by('date')[:10]
    notAttending = Events.objects.exclude (users__id = user.id, date__lt=now).order_by('date')[:10]
    feedEvents = list(itertools.chain(attending, notAttending))
    eventsShuffled = sorted(feedEvents, key=lambda x: random.random())[:10]

    results={}
    for event in eventsShuffled:
        eventList = []
        if event in attending:
            eventList.append('Going')
        else:
            eventList.append('Not Going')

        f = getFriends(user,event)

        eventList.append(f)
        results[event] = eventList

    return results
    #Only upcoming events (E se forem eventos a decorrer?)

def getFacebookFriends(user):
    
    social_user = UserSocialAuth.objects.get(user=user, provider='facebook')
    access_token = social_user.extra_data['access_token']

    if social_user:
        returned_json = requests.get("https://graph.facebook.com/v2.12/me/friends?access_token="+access_token)
        targets = returned_json.json()['data']
        
        if not targets:
            return []
        elif len(targets) ==1:
            listSocial = [targets[0]['id']]
        else:
            listSocial = [target['id'] for target in targets]
       
        friendsID = UserSocialAuth.objects.filter(uid__in=listSocial).values_list('user_id', flat=True)
        friends = User.objects.filter(id__in=friendsID)

    return friends

def addFriendships(user):

    friends = getFacebookFriends(user)
    for friend in friends:
        user.friends.add(friend)
        user.save()

def updateProfilePicture(user):

    social_user = UserSocialAuth.objects.get(user=user, provider='facebook')
    url = 'http://graph.facebook.com/{0}/picture?type=large'.format(social_user.uid)
    user.picture = url
    user.save()
   
def changeEventStatus(request):

    if request.method == "POST":
        event = Events.objects.get(pk=request.POST.get('EventId'))
        if request.POST.get('value') == "1":
            event.users.remove(User.objects.get(pk=request.user.id))
        else:
            event.users.add(User.objects.get(pk=request.user.id))

        event.save()
        return HttpResponse("Success")

def search(request):

    if request.method == "POST":

        search_string = request.POST.get('search')
        users = User.objects.filter(first_name__icontains=search_string)
        print(users)
        users = serializers.serialize('json', users)
        return JsonResponse(users,safe=False)

def get_subscribed_events(events):
    if len(events):
        return {}

    subbed_events = {}
    for ev in events:
        info = Events.objects.get(pk=ev.events.id)
        subbed_events[info.id] = {'title' : info.title, 'date' : info.date, 'time' : info.time}

    return subbed_events

def repeated_events(search):
    event_found = {}
    try: 
        evnts = Events.objects.filter(title=search).order_by('date')

        for ev in evnts:
            event_found[ev.id] = {'title' : ev.title, 'date' : ev.date, 'time': ev.time}

        return event_found
    except Exception:
        return None

def makePayment(userFrom,userTo,value,night):
    dividendo = night.dividendos.get(aDever = userFrom, cobrador = userTo)
    
    if not dividendo:
        dividendo = night.dividendos.get(aDever = userTo, cobrador = userFrom)
        if not dividendo:
            return
            #Error???
            #createDividendo errado?
            #return
        value = - value

    currentValue = dividendo.value
    if currentValue - value <= 0:
        night.dividendos.remove(dividendo)
    else:
        dividendo.update(value = currentValue - value)

    night.save()
    dividendo.save()

def addFriendToDespesa(despesa, user):
    currentValue =  despesa.amount/len(despesa.debtors.all())
    newValue = despesa.amount/(len(despesa.debtors.all())+1)

    diff = currentValue - newValue

    buyer = User.objects.get(user__id = despesa.buyer.id)#???
    night = despesa.night

    divs_aDever = night.dividendos.objects.filter(aDever=buyer)
    divs_cobrador = night.dividendos.objects.filter(cobrador=buyer)

    for div in divs_aDever:
        div.update(value = currentValue + diff)
        div.save()
    for div in divs_cobrador:
        div.update(value = currentValue - diff)
        div.save()

    despesa.debtors.add(user)
    despesa.save()

def removeFriendDespesa(despesa, user):
    currentValue =  despesa.amount/len(despesa.debtors.all())
    newValue = despesa.amount/(len(despesa.debtors.all())-1)

    diff = newValue - currentValue

    buyer = User.objects.get(user__id = despesa.buyer.id)#???
    night = despesa.night
    
    divs_aDever = night.dividendos.objects.filter(aDever=buyer)
    divs_cobrador = night.dividendos.objects.filter(cobrador=buyer)

    for div in divs_aDever:
        div.update(value = currentValue - diff)
        div.save()
    for div in divs_cobrador:
        div.update(value = currentValue + diff)
        div.save()

    despesa.debtors.remove(user)
    despesa.save()

def getCashFlows(night):
    users = night.user.all()
    N = len(users)
    pay = [[0 for x in range(N)] for y in range(N)]
    cashFlows = getCashFlowGraph(night)

    result = minCashFlow(cashFlows,N,pay)

    listUsers = []


    for i in range(len(pay)):
        for j in range(len(pay[i])):
            x = pay[i][j]
            if x!= 0:
                listUsers.append( [cashFlows[i][0],cashFlows[0][j],x])

    return listUsers

def getCashFlowGraph(night):
    #map ids - realID
    users = night.user.all().order_by('id')
   
    usersID = night.user.values_list('id', flat=True).order_by('id')

    
    num_users = len(usersID)

    graph = []
    row =[]

    row.append(0)
    for i in usersID:
        row.append(i) 
    graph.append(row)
    
    for i in usersID:
        row =[]
        row.append(i)
        for j in range(0, num_users):
            row.append(0)
        graph.append(row)

    dividendos = night.dividendos.all()
    for div in dividendos:
        aDever_id = users.filter(id__lte = div.aDever.id).count()
        cobrador_id = users.filter(id__lte = div.cobrador.id).count()

        graph[aDever_id][cobrador_id] = div.value

    return graph


def getMin(arr,N):
    minInd = 0
    for i in range(1, N):
        if (arr[i] < arr[minInd]):
            minInd = i
    return minInd

# A utility function that returns
# index of maximum value in arr[]
def getMax(arr,N):
    maxInd = 0
    for i in range(1, N):
        if (arr[i] > arr[maxInd]):
            maxInd = i
    return maxInd


# A utility function to
# return minimum of 2 values
def minOf2(x, y):
    return x if x < y else y


# amount[p] indicates the net amount to
# be credited/debited to/from person 'p'
# If amount[p] is positive, then i'th
# person will amount[i]
# If amount[p] is negative, then i'th
# person will give -amount[i]
def minCashFlowRec(amount,N,pay):
    # Find the indexes of minimum
    # and maximum values in amount[]
    # amount[mxCredit] indicates the maximum
    # amount to be given(or credited) to any person.
    # And amount[mxDebit] indicates the maximum amount
    # to be taken (or debited) from any person.
    # So if there is a positive value in amount[],
    # then there must be a negative value

    mxCredit = getMax(amount,N)
    mxDebit = getMin(amount,N)
   
    # If both amounts are 0,
    # then all amounts are settled
    if (amount[mxCredit] == 0 and amount[mxDebit] == 0):
        return 0

    # Find the minimum of two amounts
    min = minOf2(-amount[mxDebit], amount[mxCredit])
    amount[mxCredit] -= min
    amount[mxDebit] += min

    # If minimum is the maximum amount to be
    print("Person ", mxDebit, " pays ", min
          , " to ", "Person ", mxCredit)
    
    pay[mxDebit][mxCredit]= min
    
    # Recur for the amount array. Note that
    # it is guaranteed that the recursion
    # would terminate as either amount[mxCredit]
    # or amount[mxDebit] becomes 0
    minCashFlowRec(amount,N,pay)

    return (pay)


# Given a set of persons as graph[] where
# graph[i][j] indicates the amount that
# person i needs to pay person j, this
# function finds and prints the minimum
# cash flow to settle all debts.
def minCashFlow(graph,N,pay):
    # Create an array amount[],
    # initialize all value in it as 0.
    amount = [0 for i in range(N)]

    # Calculate the net amount to be paid
    # to person 'p', and stores it in amount[p].
    # The value of amount[p] can be calculated by
    # subtracting debts of 'p' from credits of 'p'
    for p in range(N):
        for i in range(N):
            amount[p] += (graph[i+1][p+1] - graph[p+1][i+1])

    pay = minCashFlowRec(amount,N,pay)

    return pay
