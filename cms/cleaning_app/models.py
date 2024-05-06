from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
from django.utils import timezone

class BaseModel(models.Model):
    """Model for subclassing."""
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
        ordering = ['-created_on']

class UserManager(BaseUserManager):        
    def create_user(self, is_active=True,username=None,email=None, password=None,role=None, uid=None):
        
        if not username:
            raise ValueError('User must have an username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            is_active=is_active, 
            role=role,
            uid=uid,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, password, email=None,role=None,uid=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            role=1,
            uid=uid,
            )
        user.is_admin = True
        user.is_active = True
        user.is_supervisor = True 
        user.save(using=self._db)
        return user
    
SELECTROLE = ((1, "admin"), (2, "supervisor"), (3, "cleners"),(4,"customer"))

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=50, unique=True, null=True)
    email = models.EmailField(max_length=100, null=True)
    role = models.IntegerField(choices=SELECTROLE)
    uid = models.CharField(max_length=500, unique=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_registered = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    
    REQUIRED_FIELDS=[]

    objects = UserManager()

    def __str__(self):
        return self.username
    class Meta:
        db_table = "user"

class UserProfile(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 25,blank=True, null=True)
    mobile_number = models.CharField(max_length=25,unique=True, null=True)
    image = models.ImageField(upload_to='profile',blank=True, null=True)

class CleaningSchedule(models.Model):
    Task_CHOICES = [
        ('vacuuming', 'Vacuuming'),
        ('mopping', 'Mopping'),
        ('dusting', 'Dusting'),
        ('sanitizing', 'Sanitizing'),
    ]

    STATUS_CHOICES = [
        ('incomplete', 'Incomplete'),
        ('complete', 'Complete'),
    ]

    scheduled_date = models.DateField(null=True, blank=True)
    area_building = models.CharField(max_length=255, null=True, blank=True)
    task = models.CharField(max_length=20, choices=Task_CHOICES, null=True, blank=True)
    assigned_user = models.ForeignKey(User, limit_choices_to={'role': 3}, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='incomplete')
    completed_date = models.DateField(null=True, blank=True)
    completed_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.scheduled_date} - {self.area_building}"
    
class Payment(BaseModel):
    cleaner = models.ForeignKey(User,limit_choices_to={'role': 3}, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=0)
    date_paid = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Payment for {self.cleaner.username} on {self.date_paid}"

class Notification(BaseModel):
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.description
    
class Feedback(BaseModel):
    cleaner = models.ForeignKey(User, limit_choices_to={'role': 3},on_delete=models.CASCADE, related_name='cleaner_feedbacks')
    work_quality = models.CharField(max_length=100)
    date_of_feedback = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback for {self.cleaner.username} - {self.date_of_feedback}"
    

##########################Modified##############################
LOCATION_CHOICES = [('Chottanikkara', 'Chottanikkara'),('Vyttila', 'Vyttila'),('Edappally', 'Edappally'),
                    ('Kaloor','Kaloor'),('High Court','High Court')]
class CustomerFlat(BaseModel):
    """
    Represents customer flat details.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    flat_number = models.CharField(max_length=20)
    floor = models.PositiveIntegerField()
    building_name = models.CharField(max_length=100)
    address = models.TextField()
    location = models.CharField(max_length=25,choices=LOCATION_CHOICES)

class CleaningPackage(BaseModel):
    """
    Represents different cleaning packages available for flats.
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class CleaningRequests(BaseModel):
    package = models.ForeignKey(CleaningPackage,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField()
    status=models.CharField(max_length=50,default='pending')
    cleaner = models.ForeignKey(User, limit_choices_to={'role': 3},on_delete=models.CASCADE,related_name='cleaner_requests',null=True)

