# Generated by Django 4.2 on 2023-07-20 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roll_cd', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='song',
            unique_together={('song_name', 'audio_file')},
        ),
    ]
