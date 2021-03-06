# Generated by Django 3.0.8 on 2020-07-18 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('topic', models.CharField(max_length=30)),
                ('author_name', models.CharField(max_length=60)),
                ('topic_subject', models.CharField(choices=[('QE', 'Quantum Electronics'), ('VL', 'VLSI Circuit Design and Device Modeling'), ('CS', 'Modern Communication Systems'), ('ME', 'Microwave Electronics')], max_length=2)),
                ('description', models.TextField()),
                ('last_modified', models.DateTimeField(auto_now_add=True)),
                ('img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
