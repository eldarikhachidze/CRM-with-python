from django.shortcuts import render
from slot.models import Slot_machine

# Create your views here.

def slot_pit(request):
    slots = Slot_machine.objects.all().order_by('slot_type')
    print(slots)
    slots_in_pit = []
    for slot in slots:
        if slot.status:
            slots_in_pit.append(slot)

    return render(request, 'slot_pit/slot_pit.html', {'slots': slots_in_pit})

def edit(request, id):
    slot = Slot_machine.objects.get(id=id)
    return render(request, 'slot/edit.html', {'slot': slot})