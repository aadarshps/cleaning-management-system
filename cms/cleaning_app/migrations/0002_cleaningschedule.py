# Generated by Django 4.2.5 on 2024-03-07 10:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cleaning_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CleaningSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('scheduled_date', models.DateField()),
                ('area_building', models.CharField(max_length=255)),
                ('schedule_type', models.CharField(choices=[('recurring', 'Recurring'), ('one_time', 'One-time'), ('ad_hoc', 'Ad-hoc')], max_length=20)),
                ('assigned_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
                'abstract': False,
            },
        ),
    ]
