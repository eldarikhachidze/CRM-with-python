from django.shortcuts import render, redirect
from chip.models import Chip
from .models import Table

# Create your views here.

def table_form(request):
    chip = Chip.objects.all().order_by('denomination')
    return render(request, 'tables/tables.html', {'chips': chip})

def create_table(request):
    if request.method == 'POST':
        denominations = request.POST.getlist('chip')
        print(denominations)
        quantities = request.POST.getlist('quantity')
        print(quantities)
        for denomination, quantity in zip(denominations, quantities):
            if int(quantity) > 0: # Only create a Table object if the quantity is greater than 0
                Table.objects.create(denomination=float(denomination), quantity=int(quantity))
                print(denomination, quantity)
    return redirect('table_form')


def table_list(request):
    tables = Table.objects.all()
    print(tables)
    return render(request, 'tables/tables.html', {'tables': tables})