# Generated by Django 3.2.25 on 2024-07-28 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='name',
            field=models.CharField(default='default_name', max_length=20),
        ),
    ]
