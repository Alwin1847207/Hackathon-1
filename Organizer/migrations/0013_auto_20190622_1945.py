# Generated by Django 2.1 on 2019-06-22 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organizer', '0012_auto_20190621_0714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventdetails',
            name='event_detail_docs',
            field=models.FileField(upload_to='images/event_details_docs/'),
        ),
        migrations.AlterField(
            model_name='organiseevent',
            name='event_poster',
            field=models.ImageField(upload_to='images/event_poster/'),
        ),
        migrations.AlterField(
            model_name='shareresource',
            name='documentFile',
            field=models.FileField(upload_to='images/shared_resources_docs/'),
        ),
        migrations.AlterField(
            model_name='shareresource',
            name='resourceImage',
            field=models.ImageField(upload_to='images/shared_resources/'),
        ),
    ]