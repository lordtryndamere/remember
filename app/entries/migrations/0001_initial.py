# Generated by Django 2.1.5 on 2019-02-06 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('date_posted', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
