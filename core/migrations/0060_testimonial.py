# Generated by Django 2.2.4 on 2020-10-14 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0059_auto_20201014_1258'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('role', models.CharField(blank=True, choices=[('Customer', 'Customer'), ('Seller', 'Seller')], max_length=100, null=True)),
                ('testimonial', models.CharField(blank=True, max_length=1000, null=True)),
                ('display', models.BooleanField(default=False)),
            ],
        ),
    ]
