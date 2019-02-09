from django.shortcuts import render
from SMSserver.models import Patient

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse
# Create your views here.
def index(request):
    """view function for the most basic homepage"""
    num_patients = Patient.objects.all().count()
    context = {'num_patients':num_patients}

    return render(request, 'index.html', context=context)


@csrf_exempt
def sms_response(request):
    # Start our TwiML response
    resp = MessagingResponse()
    # Add a text message
    msg = resp.message("Hello!! welcome!!")
    return HttpResponse(str(resp))
