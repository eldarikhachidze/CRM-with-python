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
        quantities = request.POST.getlist('quantity')

        flot = {}  # Dictionary to store denominations and quantities

        for denomination, quantity in zip(denominations, quantities):
            if int(quantity) > 0:  # Only add valid quantities
                flot[float(denomination)] = int(quantity)  # Add to the fleet dictionary

        # Create a single Table entry with the entire fleet
        if flot:
            Table.objects.create(flot=flot)

        return redirect('table_form')


def table_list(request):
    tables = Table.objects.all()
    print(tables)
    return render(request, 'tables/tables.html', {'tables': tables})