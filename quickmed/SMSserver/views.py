from django.shortcuts import render
from SMSserver.models import Patient
# Create your views here.
def index(request):
    """view function for the most basic homepage"""
    num_patients = Patient.objects.all().count()
    context = {'num_patients':num_patients}

    return render(request, 'index.html', context=context)
