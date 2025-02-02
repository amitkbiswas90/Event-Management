
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Count, Q
from django.utils.timezone import now
from django.utils import timezone
from organizar.forms import EventForm, ParticipantForm, CategoryForm
from organizar.models import Event, Participant

def home(request):
    search_query = request.GET.get('q', '').strip()
    events = Event.objects.all().order_by('-date').prefetch_related('category')
    
    if search_query:
        events = events.filter(
            Q(name__icontains=search_query) | 
            Q(location__icontains=search_query)
        )
    
    return render(request, "hero.html", {
        "events": events,
        "now": timezone.now(),
        "search_query": search_query,
    })

def create_event(request):
    event_form = EventForm()

    if request.method == "POST":
        event_form = EventForm(request.POST)
        if event_form.is_valid():
            event_form.save()
            messages.success(request, "Event create successfully!")
            return redirect('create-event')

    return render(request, "event_form.html", {"event_form": event_form})

def create_participant(request):
    form = ParticipantForm()

    if request.method == "POST":
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Participant registered successfully!")
            return redirect('create-participant')

    return render(request, "participant_form.html", {"form": form})

def create_category(request):
    category_form = CategoryForm()

    if request.method == "POST":
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            messages.success(request, "Category created successfully!")
            return redirect('create-category')

    return render(request, "category_form.html", {"category_form": category_form})

def organizer_dashboard(request):
    event_type = request.GET.get('type', 'all')  
    search_query = request.GET.get('q', '').strip()
    today_date = now().date()  

    total_pat = Participant.objects.count()

    counts = Event.objects.aggregate(
        total=Count('id'),
        upcoming=Count('id', filter=Q(date__gt=today_date)),
        past=Count('id', filter=Q(date__lt=today_date)),
        today=Count('id', filter=Q(date=today_date)), 
    )

    events = Event.objects.all().order_by("date")
    
    if search_query:
        events = events.filter(Q(name__icontains=search_query) | Q(location__icontains=search_query))
    
    if event_type == 'upcoming':
        events = events.filter(date__gt=today_date)
    elif event_type == 'past':
        events = events.filter(date__lt=today_date)
    elif event_type == 'today':
        events = events.filter(date=today_date)
    
    today_events = Event.objects.filter(date=today_date).order_by("date")
    
    return render(request, "organizer_dashboard.html", {  
        'events': events,  
        'counts': counts,  
        'total_pat': total_pat,  
        'today_events': today_events,
        'search_query': search_query,
    })

def update_event(request, id):
    event = Event.objects.get(id=id) 

    event_from = EventForm(instance=event)
    event_category_form = CategoryForm(instance=event.category if event.category else None)

    if request.method == "POST":
        event_from = EventForm(request.POST, instance=event)
        event_category_form = CategoryForm(request.POST, instance=event.category if event.category else None)

        if event_from.is_valid() and event_category_form.is_valid():
            event = event_from.save()

            event_category_form.save()

            messages.success(request, "Event Updated Successfully")
            return redirect('organizer-dashboard')  

    context = {"event_form": event_from, "category_form": event_category_form}
    return render(request, "event_form.html", context)

def delete_event(request, id):
    if request.method == 'POST':
        event = Event.objects.get(id=id)
        event.delete()
        messages.success(request, 'Event Deleted Successfully')
        return redirect('organizer-dashboard')
    else:
        messages.error(request, 'Somthing went wrong')
        return redirect('organizer-dashboard')


from django.db.models import Q

def view_event(request):
    search_query = request.GET.get('q', '').strip()
    events = Event.objects.all().order_by('-date').prefetch_related('category')
    if search_query:
        events = events.filter(Q(name__icontains=search_query) | Q(location__icontains=search_query))
    return render(request, "view_event.html", {
        "events": events,
        "now": timezone.now(),
        "search_query": search_query,
    })