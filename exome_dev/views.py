from django.shortcuts import render, get_object_or_404
from .models import Family, Patient

def index(request):
    return render(request, 'exome_dev/index.html')

def patient(request, id):
    patient = Patient.objects.get(pk=id)
    return render(request, 'exome_dev/patient.html', {'patient': patient})

def families(request):
    families = Family.objects.all()
    return render(request, 'exome_dev/families.html', {'families': families})

def family(request, family_id):
    patients = Patient.objects.filter(family_id=family_id)
    return render(request, 'exome_dev/family.html', {'family_id': family_id, 'patients': patients})