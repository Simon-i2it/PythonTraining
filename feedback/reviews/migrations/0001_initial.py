# Generated by Django 4.2 on 2023-04-29 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('feedback', models.CharField(max_length=1000)),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
