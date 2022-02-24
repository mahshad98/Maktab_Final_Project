# Generated by Django 4.0.2 on 2022-02-24 11:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mail.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Signature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Amail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=80, null=True)),
                ('body', models.TextField(blank=True, max_length=255, null=True)),
                ('mail_date', models.DateTimeField(auto_now=True)),
                ('archive', models.BooleanField(default=False, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='media/', validators=[mail.models.file_size])),
                ('trash', models.BooleanField(default=False, null=True)),
                ('category', models.ManyToManyField(related_name='amail_category', to='mail.Category')),
                ('reciever', models.ManyToManyField(related_name='amail_reciever', to=settings.AUTH_USER_MODEL)),
                ('replay', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mail.amail')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='amail_sender', to=settings.AUTH_USER_MODEL)),
                ('signature', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mail.signature')),
            ],
        ),
    ]