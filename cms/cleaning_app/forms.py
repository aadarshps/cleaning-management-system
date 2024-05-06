import datetime
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


#############################################################Modified############################################
class CustomerFlatForm(forms.ModelForm):
    class Meta:
        model = CustomerFlat
        fields = ['location','building_name','floor','flat_number','address']

    def clean_flat_number(self):
        """
        Custom validation to ensure flat_number is unique.
        """
        flat_number = self.cleaned_data.get('flat_number')
        if CustomerFlat.objects.filter(flat_number=flat_number).exists():
            raise forms.ValidationError("This flat number is already in use.")
        return flat_number

class CleaningPackageForm(forms.ModelForm):
    class Meta:
        model = CleaningPackage
        fields = ['name','description','price']

class CleanersForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'mobile_number','image']

class CleaningRequestsForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = CleaningRequests
        fields = ['package','date']
    
    def clean_date(self):
        """
        Custom validation to ensure the date is not in the past.
        """
        cleaned_date = self.cleaned_data.get('date')
        if cleaned_date < timezone.now().date():
            raise forms.ValidationError("Date cannot be in the past.")
        return cleaned_date
    
class AssignCleaningForm(forms.ModelForm):
    class Meta:
        model = CleaningRequests
        fields = ['cleaner']

STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('completed', 'Completed'),
    ]

class UpdateCleaningForm(forms.ModelForm):
    status = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.Select)
    class Meta:
        model = CleaningRequests
        fields = ['status']