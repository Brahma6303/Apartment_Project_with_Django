from django.shortcuts import render
from django.views import View
from .forms import NewMeetingForm
from .models import Meeting
# Create your views here.

class NewMeetingView(View):
    def get(self,request):
        return render(request,'meeting/new_meeting.html',{'form':NewMeetingForm})
    
    def post(self,request):
        filled_form=NewMeetingForm(request.POST,request.FILES)
        if filled_form.is_valid():
            new_meeting=Meeting(title=request.POST['title'],duration=request.POST['duration'],mom=request.FILES['mom'])
            new_meeting.save()
            return render(request,'meeting/meeting_sucess.html')