# Generated by Django 4.2 on 2023-04-28 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0006_alter_address_pin_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('code', models.CharField(max_length=2)),
            ],
        ),
        migrations.RemoveField(
            model_name='address',
            name='country',
        ),
        migrations.AddField(
            model_name='book',
            name='countries',
            field=models.ManyToManyField(to='book_outlet.country'),
        ),
    ]
