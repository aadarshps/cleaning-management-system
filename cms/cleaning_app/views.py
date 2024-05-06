
from django.shortcuts import redirect, render
from django.contrib import messages

from django.contrib.auth import authenticate, login
from cleaning_app.forms import *
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
# Your existing views...


def index(request):
   return render(request, 'index.html')

def adminhome(request):
    return render(request, 'admin_app/index.html')

def supervisor_home(request):
    return render(request,'supervisor_app/index.html')

def cleners_home(request):
    return render(request,'cleaners_app/index.html')

def signin(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            print(user,"uuuuuuuu")
            if user is not None and user.is_active:
                print("IFFFFFFFFFFFFFFFFF")
                login(request, user)
                print("signnnnnnnn")
                if user.role == 1:
                    return redirect('admin_home')
                elif user.role == 2:
                    return redirect('supervisor_home')
                elif user.role == 3:
                    return redirect('cleners_home')
                elif user.role == 4:
                    return redirect('customer-index')
            else:
                messages.info(request, 'Invalid Credentials or User is not active')
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
    return render(request, 'signin.html')

def supervisor_register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        u_form = UserRegistrationForm(request.POST)
        if form.is_valid() and u_form.is_valid():
            user = u_form.save(commit=False)
            user.role = 2
            user.is_active = True
            user.save()
            cleaners = form.save(commit=False)
            cleaners.user = user
            cleaners.save()
            return redirect('supervisor-view') 
    else:
        form = RegistrationForm()
        u_form = UserRegistrationForm()
    return render(request, 'admin_app/supervisorregister.html', {'form': form,'u_form':u_form})

def supervisor_view(request):
    usr = User.objects.filter(role=2)
    data = UserProfile.objects.filter(user__in=usr)
    return render(request, 'admin_app/supervisorview.html',{'data':data})

def cleners_view(request):
    data = User.objects.filter(role=3)
    c_data = UserProfile.objects.filter(user__in=data)
    return render(request, 'admin_app/cleaner_view.html',{'c_data':c_data})


def create_schedule(request):
    if request.method == 'POST':
        form = CleaningScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedule_list')
    else:
        form = CleaningScheduleForm()

    return render(request, 'supervisor_app/create_schedule.html', {'form': form})

def schedule_list(request):
    schedules = CleaningSchedule.objects.all()
    return render(request, 'supervisor_app/schedule_list.html', {'schedules': schedules})

def create_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Payment created successfully.')
            return redirect('payment_list')
    else:
        form = PaymentForm()
    return render(request, 'admin_app/create_payment.html', {'form': form})


def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'admin_app/payment_list.html', {'payments': payments})

def cleaner_view_payments(request):
    
    payments = Payment.objects.filter(cleaner=request.user)
    return render(request, 'cleaners_app/payment_list.html', {'payments': payments})

def supervisor_view_payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'supervisor_app/payment_list.html', {'payments': payments})

def add_notification(request):
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_notifications')
    else:
        form = NotificationForm()
    return render(request, 'admin_app/add_notification.html', {'form': form})

def view_notifications(request):
    notifications = Notification.objects.all()
    return render(request, 'admin_app/view_notifications.html', {'notifications': notifications})

def supervisor_view_notifications(request):
    notifications = Notification.objects.all()
    return render(request, 'supervisor_app/view_notifications.html', {'notifications': notifications})

def cleaner_view_notifications(request):
    notifications = Notification.objects.all()
    return render(request, 'cleaners_app/view_notifications.html', {'notifications': notifications})


def create_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_list')
    else:
        form = FeedbackForm()

    return render(request, 'supervisor_app/create_feedback.html', {'form': form})

def feedback_list(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'supervisor_app/feedback_list.html', {'feedbacks': feedbacks})


def admin_view_feedback_list(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'admin_app/feedback_list.html', {'feedbacks': feedbacks})





#################################################################CUSTOMER################################################
def customersignup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        u_form = UserRegistrationForm(request.POST)
        if form.is_valid() and u_form.is_valid():
            user = u_form.save(commit=False)
            user.role = 4
            user.is_active = True
            user.save()
            cleaners = form.save(commit=False)
            cleaners.user = user
            cleaners.save()
            return redirect('signin') 
    else:
        form = RegistrationForm()
        u_form = UserRegistrationForm()
    return render(request,'customer_register.html',{'form':form,'u_form':u_form})

def customer_index(request):
    return render(request,'customer_app/index.html')

def flat_add(request):
    if request.method == 'POST':
        form = CustomerFlatForm(request.POST)
        if form.is_valid():
            flat_instance = form.save(commit=False)
            flat_instance.user = request.user
            flat_instance.save()
            return redirect('flat-view')
    else:
        form = CustomerFlatForm()
    return render(request,'customer_app/flat-add.html',{'form':form})

def flat_view(request):
    data = CustomerFlat.objects.filter(user=request.user)
    return render(request,'customer_app/flat-view.html',{'data':data})

def package_view_customer(request):
    data = CleaningPackage.objects.all().order_by('id')
    return render(request,'customer_app/package-view.html',{'data':data})

def maid_view_customer(request):
    data = User.objects.filter(role=3)
    c_data = UserProfile.objects.filter(user__in=data)
    return render(request, 'customer_app/maid_view.html',{'c_data':c_data})

def requests_add(request):
    if request.method == "POST":
        form = CleaningRequestsForm(request.POST)
        if form.is_valid():
            instance_form = form.save(commit=False)
            instance_form.user = request.user
            instance_form.save()
            return redirect('request-view')
    else:
        form = CleaningRequestsForm()
    return render(request,'customer_app/requests_add.html',{'form':form})

def requests_view(request):
    u = request.user
    data = CleaningRequests.objects.filter(user=u)
    return render(request,'customer_app/requests_view.html',{'data':data})




######################################################################ADMIN#####################################
def customer_view_admin(request):
    data = User.objects.filter(role=4)
    c_data = UserProfile.objects.filter(user__in=data)
    return render(request, 'admin_app/customer_view.html',{'c_data':c_data})

def flat_view_admin(request):
    data = CustomerFlat.objects.all()
    return render(request,'admin_app/flat-view.html',{'data':data})

def package_add(request):
    if request.method == 'POST':
        form = CleaningPackageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('package-view')
    else:
        form = CleaningPackageForm()
    return render(request,'admin_app/package-add.html',{'form':form})

def package_view(request):
    data = CleaningPackage.objects.all().order_by('id')
    return render(request,'admin_app/package-view.html',{'data':data})

def cleaners_report(request):
    data = CleaningRequests.objects.all()
    return render(request,'admin_app/cleaners_report.html',{'data':data})


###################################################################Supervisor##########################################
def maidsignup(request):
    if request.method == 'POST':
        form = CleanersForm(request.POST,request.FILES)
        u_form = UserRegistrationForm(request.POST)
        if form.is_valid() and u_form.is_valid():
            user = u_form.save(commit=False)
            user.role = 3
            user.is_active = True
            user.save()
            cleaners = form.save(commit=False)
            cleaners.user = user
            cleaners.save()
            return redirect('maid-view') 
    else:
        form = CleanersForm()
        u_form = UserRegistrationForm()
    return render(request,'supervisor_app/maid_register.html',{'form':form,'u_form':u_form})

def maid_view(request):
    data = User.objects.filter(role=3)
    c_data = UserProfile.objects.filter(user__in=data)
    return render(request, 'supervisor_app/maid_view.html',{'c_data':c_data})

def flat_view_supervisor(request):
    data = CustomerFlat.objects.all()
    return render(request,'supervisor_app/flat-view.html',{'data':data})

def requests_view_supervisor(request):
    data = CleaningRequests.objects.all()
    return render(request,'supervisor_app/requests_view.html',{'data':data})

def assign_cleaning(request,pk):
    if request.method=='POST':
        form=AssignCleaningForm(request.POST)
        if form.is_valid():
            cleaning=CleaningRequests.objects.get(id=pk)
            cleaning.cleaner=form.cleaned_data['cleaner']
            cleaning.save()
            return redirect('request-view-supervisor')
    else:
        form=AssignCleaningForm()
    return render(request,'supervisor_app/assign_cleaning.html',{'form':form})

##############################################################################Cleaner########################################
def cleaner_schedule_view(request):
    u=request.user
    data = CleaningRequests.objects.filter(cleaner=u)
    return render(request, 'cleaners_app/cleaner_schedule_view.html', {'data':data})

def cleaner_schedule_update(request, pk):
    if request.method=='POST':
        form=UpdateCleaningForm(request.POST)
        if form.is_valid():
            cleaning=CleaningRequests.objects.get(id=pk)
            cleaning.status=form.cleaned_data['status']
            cleaning.save()
            return redirect('cleaner-schedule-view')
    else:
        form=UpdateCleaningForm()
    return render(request, 'cleaners_app/cleaner_schedule_update.html', {'form': form})

def customer_view_cleaners(request):
    data = User.objects.filter(role=4)
    c_data = UserProfile.objects.filter(user__in=data)
    return render(request, 'cleaners_app/customer_view.html',{'c_data':c_data})