# Generated by Django 3.1.4 on 2020-12-14 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_auto_20201214_0130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='room_type',
        ),
        migrations.AddField(
            model_name='room',
            name='room_type',
            field=models.ManyToManyField(to='rooms.RoomType'),
        ),
    ]
