# cleaning_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('admin_home/', views.adminhome, name='admin_home'),
    path('supervisor_home/', views.supervisor_home, name='supervisor_home'),
    path('cleners_home/', views.cleners_home, name='cleners_home'),
    path('supervisor-register/', views.supervisor_register, name='supervisor-register'),
    path('supervisor-view/', views.supervisor_view, name='supervisor-view'),
    path('cleaners-view/', views.cleners_view, name='cleaners-view'),
    path('create_schedule/',views.create_schedule, name='create_schedule'),
    path('schedule_list/',views.schedule_list, name='schedule_list'),
    path('cleaner-schedule-view/', views.cleaner_schedule_view, name='cleaner-schedule-view'),
    path('cleaner-schedule-update/<int:pk>/', views.cleaner_schedule_update, name='cleaner-schedule-update'),
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

    ##########################################################CUSTOMER##################################################
    path('customer-signup/',views.customersignup,name='customer-signup'),
    path('customer-index/',views.customer_index,name='customer-index'),
    path('flat-add/',views.flat_add,name='flat-add'),
    path('flat-view/',views.flat_view,name='flat-view'),
    path('package-view-customer/',views.package_view_customer,name='package-view-customer'),
    path('maid-view-customer/',views.maid_view_customer,name='maid-view-customer'),
    path('request-register/',views.requests_add,name='request-register'),
    path('request-view/',views.requests_view,name='request-view'),
    ##########################################################Admin##################################################
    path('customer-view-admin/',views.customer_view_admin,name='customer-view-admin'),
    path('flat-view-admin/',views.flat_view_admin,name='flat-view-admin'),
    path('package-add/',views.package_add,name='package-add'),
    path('package-view/',views.package_view,name='package-view'),
    path('cleaners-report/',views.cleaners_report,name='cleaners-report'),
    ##########################################################Supervisor######################################
    path('maid-signup/',views.maidsignup,name='maid-signup'),
    path('maid-view/',views.maid_view,name='maid-view'),
    path('flat-view-supervisor/',views.flat_view_supervisor,name='flat-view-supervisor'),
    path('request-view-supervisor/',views.requests_view_supervisor,name='request-view-supervisor'),
    path('assign/<int:pk>/',views.assign_cleaning,name='assign'),
    #########################################################Cleaners###################################
    path('customer-view-cleaners/',views.customer_view_cleaners,name='customer-view-cleaners'),

]
