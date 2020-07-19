# Generated by Django 3.0.8 on 2020-07-18 17:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('registertopics', '0002_auto_20200718_1731'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='img',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='topic',
            name='image2',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='topic',
            name='image3',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='topic',
            name='image4',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='topic',
            name='keyWords',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
