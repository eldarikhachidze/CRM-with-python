from django.shortcuts import render

# Create your views here.

def slot_pit(request):
    return render(request, 'slot_pit/slot_pit.html')