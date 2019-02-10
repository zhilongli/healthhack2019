from django.shortcuts import render
from SMSserver.models import Patient

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from twilio.twiml.messaging_response import MessagingResponse

from update import write2db

# # Create your views here.
# def index(request):
#     """view function for the most basic homepage"""
#     num_patients = Patient.objects.all().count()
#     context = {'num_patients':num_patients}

#     return render(request, 'index.html', context=context)

intro_qn = "Hi, thank you for using the YURI quick diagnosis system! Since this is your first \
time using the system, please answer a series of quick questions that follows: "
invalid_resp = "We are sorry, we don't understand that response. "
age_qn = "What is your age? Please reply in a whole number."
gender_qn = "What is your biological gender?"
cough_duration = "Have you been coughing for more than 3 weeks?"
cough_type = "Do you have phlegm?"
rash = "Do you have rashes?"
aches = "Are you experiencing aches?"
chills = "Do you have chills?"
sore_throat = "Do you have a sore throat?"
chest_pain = "Do you have chest pain?"
swelling = "Are your legs or feet swollen?"
wheezing = "Do you have wheezing?"
appetite = "Do you experience a loss of appetite?"
conclusion = "Thank you for using our system, please refer below for our recommendations.\
 We wish you a speedy recovery!"
qn_list = ["How many weeks have you been coughing?",\
"Do you have phlegm?", "Do you have wheezing?", "Do you have rashes?", "Do you have a sore throat?", "Are you experiencing aches?", "Do you have chills?",\
 "Do you experience a loss of appetite?", "Do you have a sore throat?", "Do you have chest pain?", "Are your legs or feet swollen?"]


@csrf_exempt
def sms_response(request):
    # Start our TwiML response
    resp = MessagingResponse()

    #body = environ['wsgi.input'].read(int(environ.get('CONTENT_LENGTH', 0)))
    incoming_number = request.POST.get('From', False)
    incoming_body = request.POST.get('Body', False)
    incoming_city = request.POST.get('FromCity', False)
    incoming_zip = request.POST.get('FromZip', False)


    # Add a text message=
    if incoming_body != False:
        print(incoming_body)

        res = write2db(incoming_body, incoming_number, incoming_zip)
        print(res)
        if type(res) is int:
            if res<0:
                msg = resp.message("Sad man")
            else:
                msg = resp.message(qn_list[res-1])
        else:
            msg = resp.message(res)

    return HttpResponse(str(resp))
