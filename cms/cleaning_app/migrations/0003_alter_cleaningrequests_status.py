# Generated by Django 4.2.9 on 2024-05-02 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cleaning_app', '0002_alter_cleaningrequests_cleaner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cleaningrequests',
            name='status',
            field=models.CharField(max_length=50),
        ),
    ]
