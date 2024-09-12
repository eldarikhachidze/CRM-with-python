from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
import json
from chip.models import Chip
from .models import Table

# Create your views here.

def table_form(request):
    chip = Chip.objects.all().order_by('denomination')
    return render(request, 'tables/tables.html', {'chips': chip})

def create_table(request):
    if request.method == 'POST':
        name = request.POST.get('name').upper()
        denominations = request.POST.getlist('denominations')
        quantities = request.POST.getlist('quantities')
        print(name)
        print(denominations)
        print(quantities)

        flot = {}  # Dictionary to store denominations and quantities

        for denomination, quantity in zip(denominations, quantities):
            if int(quantity) > 0:  # Only add valid quantities
                flot[float(denomination)] = int(quantity)  # Add to the fleet dictionary

        # Create a single Table entry with the entire fleet
        if not flot:
            messages.error(request, 'Please add chips to the table')
            redirect('table_form')
        elif not name:
            messages.error(request, 'Please add a name to the table')
            redirect('table_form')
        elif Table.objects.filter(name=name).exists():
            messages.error(request, 'Table already exists')
            return redirect('table_form')
        else:
            Table.objects.create(name=name, open_flot=flot, open_flot_total=sum([denomination * quantity for denomination, quantity in flot.items()]))
            print(f"Table created: {name} with flot: {flot} and total: {sum([denomination * quantity for denomination, quantity in flot.items()])}")


        return redirect('table_form')


def table_list(request):
    tables = Table.objects.all()

    for table in tables:
        if isinstance(table.close_flot, str):
            try:
                table.close_flot_dict = json.loads(table.close_flot)
            except json.JSONDecodeError:
                table.close_flot_dict = {}
        else:
            table.close_flot_dict = table.close_flot
            # If the close date is not in UTC, convert it to UTC
        if table.close_date:
            table.close_date = table.close_date + timedelta(hours=4)


    return render(request, 'tables/all_tables.html', {'tables': tables})

def table_detail(request, id):
    table = Table.objects.get(id=id)

    return render(request, 'tables/table_detail.html', {'table': table})

def table_delete(request, id):
    table = Table.objects.get(id=id)
    table.delete()

    return redirect('table_list')

def table_edit(request, id):
    table = Table.objects.get(id=id)
    date_edited = timezone.now()
    if request.method == 'POST':
        name = request.POST.get('name', '').upper()
        denominations = request.POST.getlist('denominations')
        quantities = request.POST.getlist('quantities')

        # We need a way to get the denominations, assuming you have them stored somewhere or provided in the form
        flot = {}
        for denomination, quantity in zip(denominations, quantities):
            if int(quantity) > 0:
                flot[float(denomination)] = int(quantity)

        if not flot:
            messages.error(request, 'Please add chips to the table')
            return redirect('table_edit', id=id)

        if not name:
            messages.error(request, 'Please add a name to the table')
            return redirect('table_edit', id=id)

        table.name = name
        table.open_flot = flot
        table.open_flot_total = sum([denomination * quantity for denomination, quantity in flot.items()])
        table.date_edited = date_edited
        table.save()
        messages.success(request, 'Table updated successfully')
        print(f"Table updated: {name} with flot: {flot} and total: {sum([denomination * quantity for denomination, quantity in flot.items()])}")

        return redirect('table_list')

    return render(request, 'tables/edit_table.html', {'table': table})

def close(request, id):
    table = Table.objects.get(id=id)
    date_closed = timezone.now()
    if request.method == 'POST':
        denominations = request.POST.getlist('denominations')
        quantities = request.POST.getlist('quantities')

        # We need a way to get the denominations, assuming you have them stored somewhere or provided in the form
        flot = {}
        for denomination, quantity in zip(denominations, quantities):
            flot[float(denomination)] = int(quantity)

        if not flot:
            messages.error(request, 'Please add chips to the table')
            return redirect('table_close_page', id=id)

        table.close_flot = flot
        table.close_flot_total = sum([denomination * quantity for denomination, quantity in flot.items()])
        table.result = table.close_flot_total - table.open_flot_total
        table.status = False
        table.close_date = date_closed
        table.save()
        messages.success(request, 'Table closed successfully')
        print(f"Table closed: {table.name} with flot: {flot} and total: {sum([denomination * quantity for denomination, quantity in flot.items()])}")

        return redirect('table_list')

    return render(request, 'tables/table_close.html', {'table': table})

def table_close(request, id):
    table = Table.objects.get(id=id)

    return render(request, 'tables/table_close.html', {'table': table})