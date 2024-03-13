# Generated by Django 5.0.3 on 2024-03-12 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('customrer', 'Customer'), ('employee', 'Employee')], max_length=50, null=True),
        ),
    ]
