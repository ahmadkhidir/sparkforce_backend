# Generated by Django 4.0.4 on 2022-05-26 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0002_alter_waitlistsubscribers_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waitlistsubscribers',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]