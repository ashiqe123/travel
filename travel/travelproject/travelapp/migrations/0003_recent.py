# Generated by Django 3.2.11 on 2022-04-07 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_alter_travel_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='recent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='', verbose_name='image')),
                ('head', models.CharField(max_length=120)),
                ('des', models.TextField()),
            ],
        ),
    ]
