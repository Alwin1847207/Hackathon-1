# Generated by Django 2.2.2 on 2019-08-30 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organizer', '0002_delete_sponsorshipdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organiseevent',
            name='event_poster',
            field=models.ImageField(default='images/noimage.png', upload_to='images/event_poster/'),
        ),
    ]