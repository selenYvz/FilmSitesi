# Generated by Django 3.2.12 on 2022-04-21 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filmler',
            name='kategoriler',
            field=models.ManyToManyField(to='MovieApp.kategoriler'),
        ),
    ]