# Generated by Django 3.0.8 on 2020-07-12 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='detail',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('rollno', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]