# Generated by Django 4.0.2 on 2022-03-05 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0007_remove_amail_reply_amail_reply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amail',
            name='reply',
        ),
        migrations.AddField(
            model_name='amail',
            name='reply',
            field=models.ManyToManyField(to='mail.Amail'),
        ),
    ]
