# Generated by Django 2.0.2 on 2018-04-06 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=False, upload_to='media'),
        ),
    ]
