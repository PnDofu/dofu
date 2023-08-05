# Generated by Django 4.2 on 2023-08-02 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('audio_file', models.FileField(upload_to='cd_file/')),
            ],
        ),
        migrations.CreateModel(
            name='Lyric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('lyr_file', models.FileField(upload_to='cd_lyr/')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='real_cd.song')),
            ],
        ),
    ]
