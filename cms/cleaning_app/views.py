
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
                    return redirect('adminhome')
                elif user.role == 2:
                    return redirect('supervisor_home')
                elif user.role == 3:
                    return redirect('cleners_home')
            else:
                messages.info(request, 'Invalid Credentials or User is not active')
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
    return render(request, 'signin.html')

def cleanersign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        u_form = UserRegistrationForm(request.POST)
        if form.is_valid() and u_form.is_valid():
            user = u_form.save(commit=False)
            user.role = 3
            user.is_active = True
            user.save()
            cleaners = form.save(commit=False)
            cleaners.user = user
            cleaners.save()
            return redirect('signin') 
    else:
        form = RegistrationForm()
        u_form = UserRegistrationForm()
    return render(request,'registration.html',{'form':form,'u_form':u_form})

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


def cleaner_schedule_view(request):
    u = request.user
    data = CleaningSchedule.objects.filter(assigned_user=u)

    return render(request, 'cleaners_app/cleaner_schedule_view.html', {'data':data})

def cleaner_schedule_update(request, schedule_id):
    schedule = get_object_or_404(CleaningSchedule, id=schedule_id, assigned_user=request.user)

    if request.method == 'POST':
        form = CleaningScheduleUpdateForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            return redirect('cleaner_schedule_view')
    else:
        form = CleaningScheduleUpdateForm(instance=schedule)

    return render(request, 'cleaners_app/cleaner_schedule_update.html', {'form': form, 'schedule': schedule})


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

