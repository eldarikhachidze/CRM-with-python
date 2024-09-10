from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Chip
items = []

def create(request):
    queriset = Chip.objects.all().order_by('denomination')

    print(queriset)
    error = None
    if request.method == 'POST':
        item = request.POST.get('name', '').strip()
        if item:
            try:
                denomination = float(item)
                if denomination <= 0:
                    error = "Please enter a positive number."
                elif denomination in queriset.values_list('denomination', flat=True):
                    error = f"Chip with denomination {denomination} already exists."
                else:
                    Chip.objects.create(denomination=denomination)
            except ValueError:
                error = "Please enter a valid number."
        else:
            error = "Please enter a denomination."
    return render(request, 'create_chip/chip.html', {'error': error, 'chips': queriset})

def chips(request):
    queriset = Chip.objects.all()
    print(queriset)
    return render(request, 'create_chip/chip.html', {'chips': queriset})

# def get(request, id):
#     try:
#         return HttpResponse(f'get chip by id {items[id - 1]}')
#     except:
#         return HttpResponse(f'chip with id {id} not found')

        # if check for id
    #     if id > len(items):
    #         return HttpResponse(f'chip with id {id} not found')
    #     if id <= 0:
    #         return HttpResponse(f'chip with id {id} not found')

# def update(request, id):
#     try:
#         return HttpResponse(f'update chip by id {items[id - 1]}')
#     except:
#         return HttpResponse(f'chip with id {id} not found')

def delete(request, id):
    # Get the chip with the given id
    chip = Chip.objects.get(id=id)

    # Set the date_deleted to the current time (soft delete)
    chip.date_deleted = timezone.now()
    chip.save()  # Save the change

    Chip.objects.filter(pk=id).delete()
    return redirect("create")





