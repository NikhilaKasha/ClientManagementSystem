# Generated by Django 2.2 on 2020-02-03 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0006_auto_20200202_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='vehicle',
            field=models.CharField(max_length=140, null=True),
        ),
    ]