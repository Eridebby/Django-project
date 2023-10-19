# Generated by Django 4.2.3 on 2023-07-08 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('julyapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=300)),
                ('lastname', models.CharField(max_length=300)),
                ('phonenumber', models.IntegerField()),
                ('email', models.CharField(max_length=300)),
                ('messages', models.TextField(max_length=200)),
            ],
        ),
    ]
