from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Slot_machine
# Create your views here.

def all_slot(request):
    slots = Slot_machine.objects.all().order_by('slot_type')
    return render(request, 'slot/slots.html', {'slots': slots})

def create(request):
    if request.method == 'POST':
        name = request.POST['name'].upper()
        type = request.POST['type'].upper()

        # Create a single Slot entry with the entire fleet
        if Slot_machine.objects.filter(slot_name=name).exists():
            messages.error(request, 'Slot already exists')
            return render(request, 'slot/create.html')

        Slot_machine.objects.create(slot_name=name, slot_type=type)

        return redirect('all_slot')
    return render(request, 'slot/create.html')

def delete(request, id):
    Slot_machine.objects.get(id=id).delete()

    return redirect('all_slot')

def edit(request, id):
    slot = Slot_machine.objects.get(id=id)
    return render(request, 'slot/edit.html', {'slot': slot})
