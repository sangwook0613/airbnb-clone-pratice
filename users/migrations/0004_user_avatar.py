# Generated by Django 2.2.5 on 2020-03-27 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
