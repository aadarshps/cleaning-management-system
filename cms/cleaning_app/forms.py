from django import forms
from cleaning_app.models import *


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email','password']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username is already in use')
        return username
    
    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
    
class RegistrationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'mobile_number']

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'        
 
class CleaningScheduleForm(forms.ModelForm):
    scheduled_date = forms.DateField(widget=DateInput)
    class Meta:
        model = CleaningSchedule
        fields = ['scheduled_date', 'area_building', 'task', 'assigned_user']

    def __init__(self, *args, **kwargs):
        super(CleaningScheduleForm, self).__init__(*args, **kwargs)
        # Set the default status to 'incomplete' when creating a new schedule
        # self.fields['status'].initial = 'incomplete'
        
class CleaningScheduleUpdateForm(forms.ModelForm):
    completed_date = forms.DateField(widget=DateInput)
    completed_time = forms.TimeField(widget=TimeInput)
    class Meta:
        model = CleaningSchedule
        fields = ['status', 'completed_date', 'completed_time']

    def __init__(self, *args, **kwargs):
        super(CleaningScheduleUpdateForm, self).__init__(*args, **kwargs)
        self.fields['status'].widget.attrs['enable'] = True

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['cleaner', 'amount', 'date_paid']


class NotificationForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = Notification
        fields = ['date', 'description']



class FeedbackForm(forms.ModelForm):
    date_of_feedback = forms.DateField(widget=DateInput)
    class Meta:
        model = Feedback
        fields = ['cleaner', 'work_quality', 'date_of_feedback']
