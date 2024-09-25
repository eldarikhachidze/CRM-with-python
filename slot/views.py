from django.shortcuts import render, redirect
from django.contrib import messages
from .models import SlotMachine, Hall, GameDay, SlotMachineRecord
# Create your views here.


def create_pit(request):
    halls = Hall.objects.all()

    if request.method == 'POST':
        name = request.POST['name'].upper().strip()
        if not name.strip():
            messages.error(request, 'Name is required')
            return render(request, 'slot/create_pit.html', {'halls': halls})
        elif Hall.objects.filter(name=name).exists():
            messages.error(request, 'Hall already exists')
            return render(request, 'slot/create_pit.html', {'halls': halls})
        elif not name:
            messages.error(request, 'Name is required')
            return render(request, 'slot/create_pit.html', {'halls': halls})
        else:
            Hall.objects.create(name=name)
            return redirect('create_pit')


    return render(request, 'slot/create_pit.html', {'halls': halls})

def edit_pit(request, id):
    hall = Hall.objects.get(id=id)

    return render(request, 'slot/edit_pit.html', {'hall': hall})

def delete_pit(request, id):
    Hall.objects.get(id=id).delete()

    return redirect('create_pit')

def add_slot_to_pit(request):
    if request.method == 'POST':
        hall_id = request.POST['hall']
        slot_id = request.POST['slot']

        hall = Hall.objects.get(id=hall_id)
        slot = SlotMachine.objects.get(id=slot_id)

        # Check if the slot machine is already in any hall
        for i in Hall.objects.all():
            if slot in i.slot_machines.all():
                messages.error(request, f'Slot already exists in the following halls: {i.name}.')
                return redirect('all_slot')

        # Add the slot machine to the selected hall
        hall.slot_machines.add(slot)
        messages.success(request, f'Slot added to {hall.name} successfully.')
        return redirect('all_slot')


# all slot function

def all_slot(request):
    slots = SlotMachine.objects.all().order_by('brand')
    halls = Hall.objects.prefetch_related('slot_machines').all()

    return render(request, 'slot/slots.html', {'slots': slots, 'halls': halls})

def create(request):
    if request.method == 'POST':
        name = request.POST['name'].upper()
        brand = request.POST['brand'].upper()

        # Create a single Slot entry with the entire fleet
        if SlotMachine.objects.filter(name=name).exists():
            messages.error(request, 'Slot already exists')
            return render(request, 'slot/create.html')

        SlotMachine.objects.create(name=name, brand=brand)

        return redirect('all_slot')
    return render(request, 'slot/create.html')

def delete(request, id):
    SlotMachine.objects.get(id=id).delete()

    return redirect('all_slot')

def edit(request, id):
    slot = SlotMachine.objects.get(id=id)
    return render(request, 'slot/edit.html', {'slot': slot})

