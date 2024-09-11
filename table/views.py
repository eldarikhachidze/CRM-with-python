from django.shortcuts import render, redirect
from chip.models import Chip
from .models import Table

# Create your views here.

def table_form(request):
    chip = Chip.objects.all().order_by('denomination')
    return render(request, 'tables/tables.html', {'chips': chip})

def create_table(request):
    if request.method == 'POST':
        name = request.POST.get('name').upper()
        denominations = request.POST.getlist('chip')
        quantities = request.POST.getlist('quantity')

        flot = {}  # Dictionary to store denominations and quantities

        for denomination, quantity in zip(denominations, quantities):
            if int(quantity) > 0:  # Only add valid quantities
                flot[float(denomination)] = int(quantity)  # Add to the fleet dictionary

        # Create a single Table entry with the entire fleet
        if flot:
            Table.objects.create(name=name, open_flot=flot, open_flot_total=sum([denomination * quantity for denomination, quantity in flot.items()]))
            print(f"Table created: {name} with flot: {flot} and total: {sum([denomination * quantity for denomination, quantity in flot.items()])}")


        return redirect('table_form')


def table_list(request):
    tables = Table.objects.all()

    return render(request, 'tables/all_tables.html', {'tables': tables})