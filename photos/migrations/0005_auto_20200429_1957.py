# Generated by Django 3.0.5 on 2020-04-29 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_remove_set_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='name',
        ),
        migrations.AddField(
            model_name='image',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='Tractor Show'),
        ),
    ]
