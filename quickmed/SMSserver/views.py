from django.shortcuts import render
from SMSserver.models import Patient

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from twilio.twiml.messaging_response import MessagingResponse

# # Create your views here.
# def index(request):
#     """view function for the most basic homepage"""
#     num_patients = Patient.objects.all().count()
#     context = {'num_patients':num_patients}

#     return render(request, 'index.html', context=context)


@csrf_exempt
def sms_response(request):
    # Start our TwiML response
    resp = MessagingResponse()

    #body = environ['wsgi.input'].read(int(environ.get('CONTENT_LENGTH', 0)))
    incoming_number = request.POST.get('From', False)
    incoming_body = request.POST.get('Body', False)
    incoming_city = request.POST.get('FromCity', False)

    
    # Add a text message=
    if incoming_body != False:
        print(incoming_body)
        msg = resp.message("Hi you sent "+ incoming_body)

    return HttpResponse(str(resp))
