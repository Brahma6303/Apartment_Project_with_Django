from django.shortcuts import render
from django.views import View
from .forms import NewMeetingForm
from .models import Meeting
from django.views.generic import ListView
import smtplib
from email.message import EmailMessage
import os
# Create your views here.

class NewMeetingView(View):
    def get(self,request):
        return render(request,'meeting/new_meeting.html',{'form':NewMeetingForm})
    
    def post(self,request):
        filled_form=NewMeetingForm(request.POST,request.FILES)
        if filled_form.is_valid():
            new_meeting=Meeting(title=request.POST['title'],duration=request.POST['duration'],mom=request.FILES['mom'])
            new_meeting.save()
            send_email()
            return render(request,'meeting/meeting_sucess.html')
        
#Sending email without using django
def send_email():
    email=EmailMessage() #empty email
    email['from']='my python trainer'
    #multiple emails
    to_list=['brahmaiahkanna8@gmail.com','kannabrahmaiah143@gmail.com',]
    email['to']=",".join(to_list)
    cc_list=['brahmareddymaram9@gmail.com','kannabrahmaiah143@gmail.com']
    email['cc']=",".join(cc_list)
    email['bcc']='nusimsubbareddy@gmail.com'
    #single email
    #email['to']='kannabrahmaiah1@gmail.com'
    email['subject']='About python fullstack training'
    email.set_content('Hi,This is to inform you that we have started python fullstack training from 1st April')

    #Attach file 
    with open(r"C:\Users\dell\Desktop\password.txt",'rb') as file:
        email.add_attachment(file.read(),maintype='txt',subtype='txt',filename="Letter.txt")
    #SMTP-Protocol
    with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
        smtp.starttls() #Secure connection host name and port number
        
        #password=open(r"C:\Users\dell\Desktop\password.txt").read() #hhidding the password
        
        #password=os.getenv('GMAIL_PASSWORD')
        smtp.login('kannabrahmaiah1@gmail.com',"ldnt sqdz zjnf wngg") #password this email "ldnt sqdz zjnf wngg"
        smtp.send_message(email)





class MeetingListView(ListView):
    model=Meeting
    template_name="meeting/meeting_list.html"
    context_object_name="mymeetings"