# Generated by Django 4.2 on 2023-08-03 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real_cd', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]