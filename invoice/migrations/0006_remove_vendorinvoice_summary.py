# Generated by Django 4.2.6 on 2023-10-16 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0005_alter_vendorinvoice_tax_percent_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendorinvoice',
            name='summary',
        ),
    ]