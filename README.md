# YuRI (Health Hackathon 2019)

An Automated Text System that sends diagnosis (based on a decision tree) and treatment recommendation through text messages to patients inquiring information on their respiratory problem. Implemented by integrating the *Twilio SMS System* with a *Django webhook*.

**What you need:**
- Twilio Account
- Ngrok
- Python

**How to RUn:**
1. Start an *ngrok* server
2. Copy the server's url and append "*/smsserver/*"
2. Configure this url as a webhook on the console's number page of your twilio account.
3. Navigate to the "*quickmed*" folder and run "python manage.py runserver"
4. Text any message to the twilio number and YuRI will initialize the diagnosis

**Other Features:**
While a patient is chatting with YuRI, a medical record of the patient would be automatically stored in "*database.csv*" ther "*quickmed*" folder.
    