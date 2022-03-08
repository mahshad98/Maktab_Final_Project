# Generated by Django 4.0.2 on 2022-03-05 11:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mail', '0005_amail_bcc_amail_cc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amail',
            name='bcc',
            field=models.ManyToManyField(null=True, related_name='bcc', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='amail',
            name='cc',
            field=models.ManyToManyField(null=True, related_name='cc', to=settings.AUTH_USER_MODEL),
        ),
    ]
