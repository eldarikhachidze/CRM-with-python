from django.shortcuts import render, redirect
from django.contrib import messages
from slot.models import SlotMachine, Hall

# Create your views here.

def slot_pit(request):
    halls = Hall.objects.all().order_by('name')

    return render(request, 'slot_pit/slot_pit.html', {'halls': halls})

def delete_slot_machine_from_pit(request, hall_id, slot_id):
    hall = Hall.objects.get(id=hall_id)
    slot = SlotMachine.objects.get(id=slot_id)

    hall.slot_machines.remove(slot)

    return redirect('slot_pit')