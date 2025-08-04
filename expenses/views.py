from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Entry
from .serializers import EntrySerializer
from django.shortcuts import render, redirect
from django.db.models import Sum

class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all().order_by('-date', '-time')
    serializer_class = EntrySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['type', 'category', 'currency', 'date']
    search_fields = ['description', 'category']

def report(request):
    all_entries = Entry.objects.order_by('-date', '-time')
    entries = all_entries[:100]
    total_expense = all_entries.filter(type__iexact='expense').aggregate(Sum('total_amount'))['total_amount__sum'] or 0
    total_income = all_entries.filter(type__iexact='income').aggregate(Sum('total_amount'))['total_amount__sum'] or 0
    balance = total_income - total_expense

    categories = (
        all_entries
        .filter(type__iexact='expense')
        .values('category')
        .annotate(total=Sum('total_amount'))
        .order_by('-total')
    )
    labels = [cat['category'] for cat in categories]
    data = [cat['total'] for cat in categories]

    return render(request, 'expenses/report.html', {
        'entries': entries,
        'total_expense': total_expense,
        'total_income': total_income,
        'balance': balance,
        'categories': categories,
        'labels': labels,
        'data': data,
    })

def add_entry(request):
    if request.method == 'POST':
        unit_price = float(request.POST['unit_price'])
        quantity = int(request.POST['quantity'])
        Entry.objects.create(
            type=request.POST['type'],
            category=request.POST['category'],
            unit_price=unit_price,
            quantity=quantity,
            total_amount=unit_price * quantity,  
            description=request.POST['description'],
            currency=request.POST['currency'],
        )
        return redirect('/api/report/')
    return render(request, 'expenses/add_entry.html')