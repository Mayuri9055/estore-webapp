# Generated by Django 5.0.1 on 2024-02-14 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.FloatField()),
                ('pdetails', models.CharField(max_length=50)),
                ('cat', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
