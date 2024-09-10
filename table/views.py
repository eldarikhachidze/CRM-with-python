from django.shortcuts import render
from chip.models import Chip

# Create your views here.

def table(request):
    chip = Chip.objects.all().order_by('denomination')
    return render(request, 'tables/tables.html', {'chips': chip})