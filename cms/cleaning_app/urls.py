# cleaning_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('clenersign_up/', views.cleanersign_up, name='clenersign_up'),
    path('admin_home/', views.adminhome, name='adminhome'),
    path('supervisor_home/', views.supervisor_home, name='supervisor_home'),
    path('cleners_home/', views.cleners_home, name='cleners_home'),
    path('supervisor-register/', views.supervisor_register, name='supervisor-register'),
    path('supervisor-view/', views.supervisor_view, name='supervisor-view'),
    path('cleaners-view/', views.cleners_view, name='cleaners-view'),
    path('create_schedule/',views.create_schedule, name='create_schedule'),
    path('schedule_list/',views.schedule_list, name='schedule_list'),
    path('cleaner-schedule-view/', views.cleaner_schedule_view, name='cleaner_schedule_view'),
    path('cleaner-schedule-update/<int:schedule_id>/', views.cleaner_schedule_update, name='cleaner_schedule_update'),
    path('create_payment/', views.create_payment, name='create_payment'),
    path('payment_list/', views.payment_list, name='payment_list'),
    path('cleaner_view_payments/', views.cleaner_view_payments, name='cleaner_view_payments'),
    path('supervisor_view_payment_list/', views.supervisor_view_payment_list, name='supervisor_view_payment_list'),
    path('add_notification/', views.add_notification, name='add_notification'),
    path('view_notifications/', views.view_notifications, name='view_notifications'),
    path('create_feedback/', views.create_feedback, name='create_feedback'),
    path('feedback_list/', views.feedback_list, name='feedback_list'),
    path('admin_view_feedback_list/', views.admin_view_feedback_list, name='admin_view_feedback_list'),
    path('supervisor_view_notifications/', views.supervisor_view_notifications, name='supervisor_view_notifications'),
    path('cleaner_view_notifications/', views.cleaner_view_notifications, name='cleaner_view_notifications'),
]
