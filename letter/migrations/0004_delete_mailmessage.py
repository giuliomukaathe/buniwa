# Generated by Django 4.1.7 on 2023-02-21 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letter', '0003_alter_subscribers_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MailMessage',
        ),
    ]
