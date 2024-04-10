# Generated by Django 5.0.3 on 2024-04-04 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Related',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('related_title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=500)),
                ('held_in', models.CharField(max_length=100)),
                ('held_on', models.DateTimeField()),
                ('event_photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('event_photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('event_photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('event_photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('event_photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]